__author__ = "Simon Nilsson"

import glob
import os
import shutil
from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from simba.mixins.config_reader import ConfigReader
from simba.utils.checks import (check_if_filepath_list_is_empty, check_valid_boolean, check_instance,
                                check_if_valid_input, check_that_column_exist, check_str, check_file_exist_and_readable)
from simba.utils.enums import Methods, TagNames
from simba.utils.errors import DataHeaderError, NoFilesFoundError, InvalidInputError
from simba.utils.printing import SimbaTimer, log_event, stdout_success
from simba.utils.read_write import (find_files_of_filetypes_in_directory, find_video_of_file, get_fn_ext, get_video_meta_data, read_df, write_df)

BODY_PART_TYPE = 'body-part'
ANIMAL_TYPE = 'animal'



class AdvancedInterpolator(ConfigReader):
    """
    Interpolation method that allows different interpolation parameters for different animals or body-parts.
    For example, interpolate some body-parts of animals using linear interpolation, and other body-parts of animals using nearest interpolation.

    :parameter Union[str, os.PathLike] data_dir: path to folder containing pose-estimation data or a file with pose-estimation data.
    :parameter Union[str, os.PathLike] config_path: path to SimBA project config file in Configparser format.
    :parameter Literal["animal", "body-part"] type: Type of interpolation: animal or body-part.
    :parameter Dict settings: Interpolation rules for each animal or each animal body-part.
    :parameter bool initial_import_multi_index: If True, the incoming data is multi-index columns dataframes. Use of input data is the ``project_folder/csv/input_csv`` directory. Default: False.
    :parameter bool overwrite: If True, overwrites the input data. If False, then saves input data in datetime-stamped sub-directory.

    :examples:
    >>> interpolator = AdvancedInterpolator(data_dir='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/csv/input_csv',
    >>>                                     config_path='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini',
    >>>                                     type='animal',
    >>>                                     settings={'Simon': 'linear', 'JJ': 'quadratic'}, initial_import_multi_index=True)
    >>> interpolator.run()
    """

    def __init__(self,
                 data_path: Union[str, os.PathLike],
                 config_path: Union[str, os.PathLike],
                 settings: Dict[str, Any],
                 type: Optional[Literal["animal", "body-part"]] = 'body-part',
                 multi_index_data: Optional[bool] = False,
                 overwrite: Optional[bool] = True):

        ConfigReader.__init__(self, config_path=config_path, read_video_info=False)
        check_str(name=f'{self.__class__.__name__} type', value=type, options=["animal", "body-part"], raise_error=True)
        if os.path.isfile(data_path):
            check_file_exist_and_readable(file_path=data_path)
            self.file_paths = [data_path]
        elif os.path.isdir(data_path):
            self.file_paths = find_files_of_filetypes_in_directory(directory=data_path, extensions=[f".{self.file_type}"], raise_warning=False,raise_error=True)
        else:
            raise InvalidInputError(msg=f'{data_path} is not a valid file path or file directory', source=self.__class__.__name__)
        check_valid_boolean(value=[multi_index_data, overwrite], source=self.__class__.__name__, raise_error=True)
        check_instance(source=self.__class__.__name__, instance=settings, accepted_types=(dict,))

        for animal, animal_data in settings.items():
            pass
            #if animal_data

            #
    #     log_event(logger_name=str(self.__class__.__name__), log_type=TagNames.CLASS_INIT.value, msg=f"data dir: {data_dir}, type: {type}, settings: {settings}, initial_import_multi_index: {initial_import_multi_index}, overwrite: {overwrite}")
    #     self.file_paths = find_files_of_filetypes_in_directory(
    #         directory=data_dir,
    #         extensions=[f".{self.file_type}"],
    #         raise_warning=False,
    #         raise_error=True,
    #     )
    #     check_if_valid_input(
    #         name="type", input=type, options=["animal", "body-part"], raise_error=True
    #     )
    #     self.settings, self.initial_import_multi_index, self.overwrite = (
    #         settings,
    #         initial_import_multi_index,
    #         overwrite,
    #     )
    #     self.move_dir = None
    #     if not overwrite:
    #         self.move_dir = os.path.join(
    #             data_dir, f"Pre_Advanced_Interpolation_{self.datetime}"
    #         )
    #         if not os.path.isdir(self.move_dir):
    #             os.makedirs(self.move_dir)
    #     if type == "animal":
    #         self._transpose_settings()
    #
    # def _transpose_settings(self):
    #     """Helper to transpose settings dict if interpolating per animal, so the same method can be used for both animal and body-part interpolation"""
    #     transposed_settings = {}
    #     for animal_name, body_part_data in self.animal_bp_dict.items():
    #         transposed_settings[animal_name] = {}
    #         for animal_body_part in body_part_data["X_bps"]:
    #             transposed_settings[animal_name][animal_body_part[:-2]] = self.settings[
    #                 animal_name
    #             ]
    #     self.settings = transposed_settings
    #
    # def run(self):
    #     for file_cnt, file_path in enumerate(self.file_paths):
    #         df = (
    #             read_df(
    #                 file_path=file_path,
    #                 file_type=self.file_type,
    #                 check_multiindex=self.initial_import_multi_index,
    #             )
    #             .fillna(0)
    #             .reset_index(drop=True)
    #         )
    #         _, video_name, _ = get_fn_ext(filepath=file_path)
    #         if self.initial_import_multi_index:
    #             if len(df.columns) != len(self.bp_col_names):
    #                 raise DataHeaderError(
    #                     msg=f"The SimBA project suggest the data should have {len(self.bp_col_names)} columns, but the input data has {len(df.columns)} columns",
    #                     source=self.__class__.__name__,
    #                 )
    #             df.columns = self.bp_headers
    #         df[df < 0] = 0
    #         for animal_name, animal_body_parts in self.settings.items():
    #             for bp, interpolation_setting in animal_body_parts.items():
    #                 check_that_column_exist(
    #                     df=df, column_name=f"{bp}_x", file_name=file_path
    #                 )
    #                 check_that_column_exist(
    #                     df=df, column_name=f"{bp}_y", file_name=file_path
    #                 )
    #                 df[[f"{bp}_x", f"{bp}_y"]] = df[[f"{bp}_x", f"{bp}_y"]].astype(int)
    #                 idx = df.loc[
    #                     (df[f"{bp}_x"] <= 0.0) & (df[f"{bp}_y"] <= 0.0)
    #                 ].index.tolist()
    #                 print(
    #                     f"Interpolating {len(idx)} {bp} body-parts in video {video_name}..."
    #                 )
    #                 df.loc[idx, [f"{bp}_x", f"{bp}_y"]] = np.nan
    #                 df[[f"{bp}_x", f"{bp}_y"]] = (
    #                     df[[f"{bp}_x", f"{bp}_y"]]
    #                     .interpolate(method=interpolation_setting, axis=0)
    #                     .ffill()
    #                     .bfill()
    #                     .astype(int)
    #                 )
    #                 df[[f"{bp}_x", f"{bp}_y"]][df[[f"{bp}_x", f"{bp}_y"]] < 0] = 0
    #         if self.initial_import_multi_index:
    #             multi_idx_header = []
    #             for i in range(len(df.columns)):
    #                 multi_idx_header.append(
    #                     ("IMPORTED_POSE", "IMPORTED_POSE", list(df.columns)[i])
    #                 )
    #             df.columns = pd.MultiIndex.from_tuples(multi_idx_header)
    #         if not self.overwrite:
    #             shutil.move(
    #                 src=file_path,
    #                 dst=os.path.join(self.move_dir, os.path.basename(file_path)),
    #             )
    #         write_df(
    #             df=df,
    #             file_type=self.file_type,
    #             save_path=file_path,
    #             multi_idx_header=self.initial_import_multi_index,
    #         )
    #     self.timer.stop_timer()
    #     stdout_success(
    #         msg="Interpolation complete!",
    #         elapsed_time=self.timer.elapsed_time_str,
    #         source=self.__class__.__name__,
    #     )

SMOOTHING_SETTINGS = {'Simon': {'Ear_left_1': {'method': 'Savitzky Golay', 'time_window': 3500},
                               'Ear_right_1': {'method': 'Gaussian', 'time_window': 500},
                               'Nose_1': {'method': 'Savitzky Golay', 'time_window': 2000},
                               'Lat_left_1': {'method': 'Savitzky Golay', 'time_window': 2000},
                               'Lat_right_1': {'method': 'Gaussian', 'time_window': 2000},
                               'Center_1': {'method': 'Savitzky Golay', 'time_window': 2000},
                               'Tail_base_1': {'method': 'Gaussian', 'time_window': 500}},
                        'JJ': {'Ear_left_2': {'method': 'Savitzky Golay', 'time_window': 2000},
                               'Ear_right_2': {'method': 'Savitzky Golay', 'time_window': 500},
                               'Nose_2': {'method': 'Gaussian', 'time_window': 3500},
                               'Lat_left_2': {'method': 'Savitzky Golay', 'time_window': 500},
                               'Lat_right_2': {'method': 'Gaussian', 'time_window': 3500},
                               'Center_2': {'method': 'Gaussian', 'time_window': 2000},
                               'Tail_base_2': {'method': 'Savitzky Golay', 'time_window': 3500}}}



AdvancedInterpolator(config_path='/Users/simon/Desktop/envs/simba/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini',
                     data_path='/Users/simon/Desktop/envs/simba/troubleshooting/two_black_animals_14bp/project_folder/new_data',
                     settings=SMOOTHING_SETTINGS, type='body-part', multi_index_data=True, overwrite=True)