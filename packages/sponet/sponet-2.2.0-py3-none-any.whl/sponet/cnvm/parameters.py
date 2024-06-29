from __future__ import annotations
from dataclasses import dataclass, field
import networkx as nx
import numpy as np

from ..network_generator import NetworkGenerator


@dataclass()
class CNVMParameters:
    """
    Container for the parameters of the Continuous-time Noisy Voter Model (CNVM).

    A node i transitions from its current opinion m to a different opinion n at rate
    r[m,n] * d(i,n) / (d(i)^alpha) + r_tilde[m,n],
    where d(i,n) is the count of opinion n in the neighborhood of agent i, and d(i) the degree of node i.

    Either a network has to specified, or a NetworkGenerator,
    or num_agents, in which case a complete network is used.
    If multiple are given, NetworkGenerator overrules network, and network overrules num_agents.

    The rate parameters r and r_tilde can be given as numpy arrays of shape (num_opinions, num_opinions),
    or as floats, in which case all rates are set to this value.

    (Internally, the CNVM uses an equivalent set of rate parameters: r_imit, r_noise, prob_imit and prob_noise.
    A node i transitions from its current opinion m to a different opinion n at rate
    r_imit * d(i,n) / (d(i)^alpha) * prob_imit[m, n] + r_noise * (1/num_opinions) * prob_noise[m, n].
    These parameters can be provided instead of the usual r and r_tilde.)
    """

    num_opinions: int
    num_agents: int = None
    network: nx.Graph | None = field(default=None, repr=False)
    network_generator: NetworkGenerator | None = None
    alpha: float = 1

    # rate parameters in style 1
    r: float | np.ndarray = None
    r_tilde: float | np.ndarray = None

    # rate parameters in style 2
    r_imit: float = None
    r_noise: float = None
    prob_imit: float | np.ndarray = 1
    prob_noise: float | np.ndarray = 1

    def __post_init__(self):
        # rates
        self._tidy_up_rates()

        # networks
        if self.network_generator is not None:
            self.num_agents = self.network_generator.num_agents
            self.network = None
        elif self.network is not None:
            self.num_agents = len(self.network.nodes)
        elif self.num_agents is None:
            raise ValueError(
                "Either a network or a NetworkGenerator or num_agents has to be specified."
            )

    def _tidy_up_rates(self):
        """
        Check if the given rate parameters are valid and set up the other rate parameters accordingly.
        """
        one_mat = np.ones((self.num_opinions, self.num_opinions))
        if self.r is not None and self.r_tilde is not None:  # style 1
            if isinstance(self.r, (float, int)):
                self.r = self.r * one_mat
            if isinstance(self.r_tilde, (float, int)):
                self.r_tilde = self.r_tilde * one_mat
            np.fill_diagonal(self.r, 0)
            np.fill_diagonal(self.r_tilde, 0)

            if np.min(self.r) < 0 or np.min(self.r_tilde) < 0:
                raise ValueError("Rates have to be non-negative.")

            (
                self.r_imit,
                self.r_noise,
                self.prob_imit,
                self.prob_noise,
            ) = convert_rate_to_cnvm(self.r, self.r_tilde)

        elif self.r_imit is not None and self.r_noise is not None:  # style 2
            if isinstance(self.prob_imit, (float, int)):
                self.prob_imit = self.prob_imit * one_mat
            if isinstance(self.prob_noise, (float, int)):
                self.prob_noise = self.prob_noise * one_mat
            np.fill_diagonal(self.prob_imit, 0)
            np.fill_diagonal(self.prob_noise, 0)

            if np.min(self.r_imit) < 0 or np.min(self.r_noise) < 0:
                raise ValueError("Rates have to be non-negative.")
            if np.min(self.prob_imit) < 0 or np.max(self.prob_imit) > 1:
                raise ValueError("Probabilities have to be between 0 and 1.")
            if np.min(self.prob_noise) < 0 or np.max(self.prob_noise) > 1:
                raise ValueError("Probabilities have to be between 0 and 1.")

            self.r = self.r_imit * self.prob_imit
            self.r_tilde = self.r_noise * self.prob_noise / self.num_opinions

        else:
            raise ValueError("Rate parameters have to be provided.")

    def change_rates(
        self, r: float | np.ndarray = None, r_tilde: float | np.ndarray = None
    ):
        """
        Change one or both rate parameters.

        If only one argument is given, the other rate parameter stays the same.

        Parameters
        ----------
        r : float | np.ndarray, optional
        r_tilde : float | np.ndarray
        """
        if r is not None:
            self.r = r
        if r_tilde is not None:
            self.r_tilde = r_tilde
        self._tidy_up_rates()

    def get_network(self) -> nx.Graph:
        """
        If self.network exists, returns the network.
        Else, if a NetworkGenerator was given, returns a network generated by it.
        Else, returns the complete graph.

        Returns
        -------
        nx.Graph
        """
        if self.network is not None:
            return self.network
        elif self.network_generator is not None:
            return self.network_generator()
        else:
            return nx.complete_graph(self.num_agents)

    def set_network(self, network: nx.Graph) -> None:
        """
        Set new network.

        Only works if no NetworkGenerator was given.

        Parameters
        ----------
        network : nx.Graph
        """
        if self.network_generator is not None:
            raise ValueError("Cannot set network when there is a NetworkGenerator.")
        self.network = network
        self.num_agents = len(network.nodes)

    def update_network_by_generator(self) -> None:
        """
        Update self.network via the NetworkGenerator.

        Only works if a NetworkGenerator was given.
        """
        if self.network_generator is None:
            raise ValueError("No NetworkGenerator was given.")
        self.network = self.network_generator()


def save_params_as_txt_file(filename: str, params: CNVMParameters):
    """
    Save parameters as a readable .txt file.

    Parameters
    ----------
    filename : str
    params : CNVMParameters
    """
    if filename[-4:] != ".txt":
        this_filename = filename + ".txt"
    else:
        this_filename = filename

    with open(this_filename, "w") as f:
        f.write(f"num_agents = {params.num_agents}\n")
        f.write(f"num_opinions = {params.num_opinions}\n")
        f.write(f"alpha = {params.alpha}\n")
        f.write(f"r_imit = {params.r_imit}\n")
        f.write(f"r_noise = {params.r_noise}\n\n")
        f.write(f"prob_imit =\n {params.prob_imit}\n\n")
        f.write(f"prob_noise =\n {params.prob_noise}\n\n")

        if params.network_generator is not None:
            f.write(f"network_generator = {params.network_generator}\n")
        elif params.network is not None:
            f.write(f"network = {params.network}\n")
        else:
            f.write(f"network = fully connected\n")


def convert_rate_to_cnvm(
    r: np.ndarray, r_tilde: np.ndarray
) -> tuple[float, float, np.ndarray, np.ndarray]:
    """
    Convert the rates r and r_tilde to the parameters used in the CNVM, i.e., r_imit, r_noise, prob_imit, prob_noise.

    The rates r and r_tilde are defined as:
    An agent i transitions from his current opinion m to a different opinion n at rate
    r[m, n] * d(i,n) / (d(i)^alpha) + r_tilde[m, n]
    where d(i,n) is the count of opinion n in the neighborhood of agent i, and d(i) the degree of node i.

    Parameters
    ----------
    r : np.ndarray
        shape = (num_opinions, num_opinions)
    r_tilde : np.ndarray
        shape = (num_opinions, num_opinions)

    Returns
    -------
    tuple[float, float, np.ndarray, np.ndarray]
        r_imit, r_noise, prob_imit, prob_noise
    """
    num_opinions = r.shape[0]

    # r[m,n] = r_imit * prob_imit[m,n]
    this_r = np.copy(r)
    np.fill_diagonal(this_r, 0)
    r_imit = np.max(this_r)
    if r_imit > 0:
        prob_imit = this_r / r_imit
    else:
        prob_imit = np.zeros((num_opinions, num_opinions))

    # r_tilde[m, n] = r_noise / num_opinions * prob_noise[m, n]
    this_r_tilde = np.copy(r_tilde)
    np.fill_diagonal(this_r_tilde, 0)
    r_noise = np.max(this_r_tilde) * num_opinions
    if r_noise > 0:
        prob_noise = this_r_tilde * num_opinions / r_noise
    else:
        prob_noise = np.zeros((num_opinions, num_opinions))

    return r_imit, r_noise, prob_imit, prob_noise


def convert_rate_from_cnvm(params: CNVMParameters) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert the rates used in the CNVM to r and r_tilde.

    The rates r and r_tilde are defined as:
    An agent i transitions from his current opinion m to a different opinion n at rate
    r[m, n] * d(i,n) / (d(i)^alpha) + r_tilde[m, n]
    where d(i,n) is the count of opinion n in the neighborhood of agent i, and d(i) the degree of node i.

    Parameters
    ----------
    params : CNVMParameters

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        r, r_tilde
    """
    r = params.r_imit * params.prob_imit
    r_tilde = params.r_noise * params.prob_noise / params.num_opinions
    return r, r_tilde
