import os
from typing import Annotated

import typer
import whatthepatch

from ppatch.app import app, logger
from ppatch.model import Diff, File
from ppatch.utils.parse import wtp_diff_to_diff
from ppatch.utils.resolve import apply_change


@app.command()
def apply(
    filename: str,
    patch_path: str,
    reverse: Annotated[bool, typer.Option("-R", "--reverse")] = False,
    fuzz: Annotated[int, typer.Option("-F", "--fuzz")] = 0,
):
    """
    Apply a patch to a file.
    """
    if not os.path.exists(filename):
        logger.error(f"Warning: {filename} not found!")
        return

    if not os.path.exists(patch_path):
        logger.error(f"Warning: {patch_path} not found!")
        return

    logger.info(f"Apply patch {patch_path} to {filename}")

    origin_file = File(file_path=filename)
    new_line_list = origin_file.line_list

    with open(patch_path, mode="r", encoding="utf-8") as (f):
        diffes = whatthepatch.parse_patch(f.read())

        for diff in diffes:
            diff = wtp_diff_to_diff(diff)
            if diff.header.old_path == filename or diff.header.new_path == filename:
                apply_result = apply_change(
                    diff.hunks, new_line_list, reverse=reverse, fuzz=fuzz
                )
                # TODO: 检查失败数
                new_line_list = apply_result.new_line_list
            else:
                logger.info(f"Do not match with {filename}, skip")
    # new_line_list, _ = _apply(patch_path, filename, new_line_list, "default")

    # 写入文件
    with open(filename, mode="w+", encoding="utf-8") as (f):
        for line in new_line_list:
            if line.status:
                f.write(line.content + "\n")
