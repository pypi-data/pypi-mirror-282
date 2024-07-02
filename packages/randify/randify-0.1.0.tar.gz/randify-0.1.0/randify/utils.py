import numpy as np
from KDEpy import TreeKDE


def _extract_samples_from_ranvar(*args):
    """
    Helper function for extracting samples from multiple RandomVariables
    The samples are concatenated into a single array.
    :param *args: RandomVariable objects.
    :return: np.ndarray, Concatenated samples of all RandomVariable objects.
    """
    N_samples_per_ranvar = [len(ranvar._samples) for ranvar in args]
    sample_initial_shapes = [np.shape(ranvar.example_sample) for ranvar in args]
    samples_total = np.zeros((min(N_samples_per_ranvar), 0))
    for ranvar in args:
        samples_ranvar = ranvar._samples[: min(N_samples_per_ranvar)]
        samples_ranvar = np.array([np.reshape(sample, -1) for sample in samples_ranvar])
        samples_total = np.concatenate((samples_total, samples_ranvar), axis=1)

    return samples_total, sample_initial_shapes


def _extract_given_samples(*args, sample_inital_shapes):
    """
    Helper function for extracting given samples that are given as seperate arguments.
    The samples are concatenated into a single array.
    :param *args: multiple lists or np.ndarrays of samples
    :return: np.ndarray, Concatenated samples of all RandomVariable objects.
    """
    if len(args) != len(sample_inital_shapes):
        raise ValueError("Number of given samples does not match number of RandomVariables.")
    else:
        given_samples = None
        for ranvar_values, sample_initial_shape in zip(args, sample_inital_shapes):
            if np.shape(ranvar_values) == sample_initial_shape:
                if given_samples is None:
                    given_samples = np.reshape(ranvar_values, (1, -1))
                else:
                    given_samples = np.concatenate(
                        (given_samples, np.reshape(ranvar_values, (1, -1))), axis=1
                    )
            elif np.shape(ranvar_values)[1:] == sample_initial_shape:
                if given_samples is None:
                    given_samples = np.reshape(ranvar_values, (np.shape(ranvar_values)[0], -1))
                else:
                    given_samples = np.concatenate(
                        (
                            given_samples,
                            np.reshape(ranvar_values, (np.shape(ranvar_values)[0], -1)),
                        ),
                        axis=1,
                    )
            else:
                raise ValueError(
                    "Shape of given samples does not match shape of RandomVariable samples."
                )

    return given_samples


def pdf(*args, kernel="gaussian", bandwidth=None):
    """
    Calculate the probability density function of one or multiple RandomVariables.
    Based on a kernel density estimation using KDEpy.
    Examples:
    .. code-block:: python
        x1 = RandomVariable(np.random.normal, loc=0, scale=1)
        x2 = RandomVariable(np.random.normal, loc=0, scale=1)
        x3 = RandomVariable(np.random.multivariate_normal, mean=np.zeros(2,), cov=np.eye(2))
        pdf(x1)(0) # will give the marginal pdf of x1 evaluated at x1=0.
        pdf(x1, x2)(0,0) # will give the joint pdf of x1 and x2 evaluated at x1=0, x2=0.
        pdf(x3)([0,0]) # will give the pdf of x3 evaluated at x3=[0,0].
        pdf(x1, x3)(0,[0,0]) # will give the joint pdf of x1 and x3 evaluated at x1=0, x3=[0,0].
    The function allows multiple values at once if they are stacked along the 0-th axis:
    .. code-block:: python
        pdf(x1, x3)([0,1], [[0,0], [1,1]]) # will give the pdf at x1=0, x3=[0,0] and x1=1, x3=[1,1].
    :param *args: RandomVariable objects to calculate the joint probability density function of.
    :param kernel: Kernel for the kernel density estimation. Default "gaussian".
    :param bandwidth: Bandwidth for the kernel density estimation. Default None.
        None will estimate the bandwidth automatically.
    :return: Probability density function at given input.
    """
    if len(args) == 1 and hasattr(args[0], "_pdf_foo"):
        # check for cached pdf function if only one RandomVariable is involved
        return args[0]._pdf_foo
    else:
        samples_total, sample_inital_shapes = _extract_samples_from_ranvar(*args)
        if bandwidth is None:
            # https://www.stat.rice.edu/~scottdw/ss.nh.pdf, page 17
            bandwidth = np.min(np.std(samples_total, axis=0)) * samples_total.shape[0] ** (
                -1 / (samples_total.shape[1] + 4)
            )
        kde = TreeKDE(kernel=kernel, bw=bandwidth).fit(samples_total)

        def _pdf(*args):
            x = _extract_given_samples(*args, sample_inital_shapes=sample_inital_shapes)
            pdf_value = kde.evaluate(x)
            if len(pdf_value) == 1:
                return pdf_value[0]
            else:
                return pdf_value

        if len(args) == 1:
            # cache pdf function to RandomVariable object
            args[0]._pdf_foo = _pdf

        return _pdf


def cov(*args):
    """
    Calculate the covariance matrix of one or multiple RandomVariables.
    :param *args: RandomVariable objects.
    :return: np.ndarray, Covariance matrix of all RandomVariable objects.
    """
    samples_total, sample_inital_shapes = _extract_samples_from_ranvar(*args)
    return np.cov(samples_total, rowvar=False)
