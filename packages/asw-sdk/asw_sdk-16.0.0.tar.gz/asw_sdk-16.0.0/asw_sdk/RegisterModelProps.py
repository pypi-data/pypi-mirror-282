class RegisterModelProps:
    """
    A class used to represent the properties required to register a model.

    Attributes
    ----------
    model_id : str
        The unique identifier for the model.
    model_location : str
        The location where the model is stored.
    is_active : bool
        A flag indicating if the model is currently active.
    **kwargs : dict
        Additional keyword arguments.

    Methods
    -------
    __init__(self, model_id, model_location, is_active, **kwargs)
        Initializes the RegisterModelProps instance.
    """

    def __init__(self, model_id, model_location, is_active, **kwargs):
        """
        Initialize the RegisterModelProps instance.

        Parameters
        ----------
        model_id : str
            The unique identifier for the model.
        model_location : str
            The location where the model is stored.
        is_active : bool
            A flag indicating if the model is currently active.
        **kwargs : dict
            Additional keyword arguments.
        """
        self.model_id = model_id
        self.model_location = model_location
        self.is_active = is_active
        for key, value in kwargs.items():
            setattr(self, key, value)
