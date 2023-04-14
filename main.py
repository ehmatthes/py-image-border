from cli_args import parse_cli_args
from image_processing import add_border_to_image

def main():
    # Get the filename and optional CLI args.
    args = parse_cli_args()

    # Add border to image and save the new image.
    new_img_path = add_border_to_image(args)
    print(f"New image saved at {new_img_path}")

if __name__ == "__main__":
    main()
