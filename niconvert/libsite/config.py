from ..libcore.filter import CustomFilter


class Config(object):

    def __init__(self, args):
        self.args = args
        self.assist_params = self._assist_params()
        self.custom_filter = self._custom_filter()
        self.disable_bottom_filter = self._disable_bottom_filter()
        self.disable_guest_filter = self._disable_guest_filter()
        self.disable_video_filter = self._disable_video_filter()
        self.skip_patch = self._skip_patch()
        self.merge_parts = self._merge_parts()

    def _assist_params(self):
        if not self.args['assist_params']:
            return {}
        params = {}
        for pair in self.args['assist_params'].split(','):
            key, value = pair.split('=')
            params[key] = value
        return params

    def _custom_filter(self):
        if not self.args['custom_filter']:
            return []
        filename = self.args['custom_filter']
        with open(filename) as file:
            lines = file.read().strip() + '\n'

        return CustomFilter(lines)

    def _disable_bottom_filter(self):
        return self.args['disable_bottom_filter']

    def _disable_guest_filter(self):
        return self.args['disable_guest_filter']

    def _disable_video_filter(self):
        return self.args['disable_video_filter']

    def _skip_patch(self):
        return self.args['skip_patch']

    def _merge_parts(self):
        return self.args['merge_parts']
