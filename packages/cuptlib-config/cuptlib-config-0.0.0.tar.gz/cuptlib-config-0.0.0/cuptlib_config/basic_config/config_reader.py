from typing import Any, Dict
from configparser import ConfigParser

def save_config_dict(data: Dict[str, Dict[str, Any]], file_path: str = "config.ini"):
    """
    Save configuration data to a ConfigParser object and write it to a config file.

    Parameters:
        data (Dict[str, Dict[str, Any]]): A dictionary containing configuration data to be saved.
            Each key represents a section, and its value is another dictionary of key-value pairs.
        file_path (str): Path to the config file. Defaults to "config.ini" in the current directory.

    Raises:
        IOError: If there is an error while writing the configuration data to the config file.
    """
    config = ConfigParser()

    for section, section_data in data.items():
        config[section] = {k: str(v) for k, v in section_data.items()}

    try:
        with open(file_path, "w") as f:
            config.write(f)
    except IOError as e:
        raise IOError(f"Error writing config file: {str(e)}")

def load_config(config_class, file_path: str = "config.ini"):
    """
    Load and parse configuration settings from a config file.

    Parameters:
        config_class: configclass
        file_path (str): Path to the config file. Defaults to "config.ini" in the current directory.

    Returns:
        Dict[str, Dict[str, Any]]: A dictionary containing the parsed configuration settings.
    """
    config = ConfigParser()
    config.read(file_path)

    config_dict = {}
    for section in config.sections():
        config_dict[section] = {}
        for key, value in config[section].items():
            # Try to convert the value to int or float if possible
            try:
                config_dict[section][key] = int(value)
            except ValueError:
                try:
                    config_dict[section][key] = float(value)
                except ValueError:
                    config_dict[section][key] = value
                    
    return config_class.dict_to_object(config_dict)

# Example usage:
if __name__ == "__main__":

    import os
    from basic_config.configclasses import configclass
    
    config_dict = {
        'param': 
            {'name': 'sample', 'load_dir': 'load', 'save_dir': 'save', 'image_dir': 'image_dir', 'param_dir': 'param_dir', }, 
        'path': 
            {'beam_energy': 10, 'dps': 7.5e-05, 'sdd': 1.3, 'wavelength': 1239.8419843320025}
    }
    
    config_path = os.path.join(__file__, "../sample.ini")
    save_config_dict(config_dict, config_path)
    
    @configclass
    class ConfigurationPaths:

        load_dir: str = "load_dir"
        save_dir: str = "save_dir"
        
        param_dir: str = "param_dir"
        image_dir: str = "image_dir"
        
        def __post_init__(self) -> None:
            self.param_dir = os.path.join(self.save_dir, self.param_dir)
            self.image_dir = os.path.join(self.save_dir, self.image_dir)
            
    @configclass
    class ConfigurationParameters:

        name: str = "name"
        sdd: float = 1.3
        dps: float = 7.5e-5
        beam_energy: float = 10

        def __post_init__(self) -> None:
            self.wavelength = 12398.419843320025 / self.beam_energy  # Wavelength of Xray in Angstrom.
            
    @configclass
    class ExperimentConfiguration():

        param: ConfigurationParameters = ConfigurationParameters()
        path: ConfigurationPaths = ConfigurationPaths()

    config_object = ExperimentConfiguration.dict_to_object(config_dict)
    print("Loaded config object:\n", config_object)