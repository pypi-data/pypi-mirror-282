

class Config(object):

    def __init__(self, *args, **kwargs):

        self.work_dir = kwargs.get('work_dir', '/simulations')
        self.n_proc = kwargs.get('n_proc', 12)


config = Config()
