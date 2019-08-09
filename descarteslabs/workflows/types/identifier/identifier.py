from descarteslabs.common.graft import client as graft_client
from ..core.core import is_generic


def parameter(name, type_):
    """
    Create a typed parameter.

    Useful for describing computations that will be further
    parameterized at runtime.

    To actually provide values for the parameter at `Job` compute time,
    pass them in as keyword arguments to `.compute`.

    Parameters
    ----------
    name: str
        Name of the parameter
    type_: ProxyType
        Type of the parameter

    Returns
    -------
    proxyTime:
        a ProxyType object of type `type_`.

    Example
    -------
    >>> from descarteslabs.workflows import Float, parameter
    >>> my_program = Float(0.42) * parameter("scale", Float)
    >>> my_program.compute(scale=wf.Float(0.99))  # doctest: +SKIP
    """

    if name.isdigit():
        raise ValueError("Parameter name cannot be a digit")

    if is_generic(type_):
        raise ValueError(
            "Parameter type cannot be generic, must be concrete (like List[Int], not plain List)"
        )

    return identifier(name, type_)


def identifier(name, type_):
    """
    Create a Proxytype instance that references a graft key; i.e. for references to builtin constants or parameters.
    """
    return type_._from_graft(graft_client.keyref_graft(name))