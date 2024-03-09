import zipfile
import os
from re import sub
from x4tweaker.lib.interfaces import IXmlMod

class ModBundle():
    def __init__(self, bundle_name: str, bundle_output_path: str) -> None:
        """
        Mod bundler

        This class is used to bundle multiple mods into a single project.

        :param bundle_name: The name of the mod bundle without extension.
        :param bundle_output_path: The path with the file name and without the extension, where the mod bundle will be saved.
        """
        name = '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            bundle_name.replace('-', ' '))).split()
        ).lower()
        self.name = name
        self.output_path = bundle_output_path
        self.mods = []

    def add_xml(self, mod: IXmlMod):
        """
        Adds an XML mod to the bundle.

        :param mod: The mod to add to the bundle.
        """
        self.mods.append(mod)
        return self
    
    def build(self):
        """
        Builds the mod bundle to the disk.
        """
        # remove file extension from output path
        path = os.path.splitext(self.output_path)[0]
        # FIXME: Can't override existing files
        with zipfile.ZipFile(str(path) + ".zip", "w") as z:
            for mod in self.mods:
                z.writestr(os.path.join(self.name, mod.get_path), mod.get_xml)
