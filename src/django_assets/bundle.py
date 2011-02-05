from django.contrib.staticfiles import finders
from webassets.bundle import Bundle


class StaticBundle(Bundle):
    
    def get_files(self, env=None):
        """Return a flattened list of all source files of this bundle,
        and all the nested bundles.
        """
        env = self._get_env(env)
        files = []
        for c in self.resolve_contents(env):
            if isinstance(c, Bundle):
                files.extend(c.get_files(env))
            else:
                files.append(finders.find(c))
        return files