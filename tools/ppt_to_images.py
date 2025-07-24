import argparse
import os
from pptx2img.converter import PPTXConverter, FileHandlingError, ConversionError, LibreOfficeNotFoundError


def ppt_to_images(pptx_path: str, output_dir: str) -> None:
    """指定されたPPTXファイルを画像化する"""
    converter = PPTXConverter()
    try:
        converter.convert_pptx_to_images(pptx_path, output_dir)
    except (FileHandlingError, ConversionError, LibreOfficeNotFoundError) as e:
        raise RuntimeError(f"変換に失敗しました: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="PowerPointを画像に変換するツール")
    parser.add_argument("pptx", help="変換したいPPTXファイルのパス")
    parser.add_argument("output_dir", help="出力先ディレクトリ")
    args = parser.parse_args()

    pptx_path = os.path.abspath(args.pptx)
    output_dir = os.path.abspath(args.output_dir)
    ppt_to_images(pptx_path, output_dir)
    print(f"画像を {output_dir} に出力しました")


if __name__ == "__main__":
    main()

