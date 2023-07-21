from PIL import Image
import os

def convert_to_png(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for root, _, filenames in os.walk(input_folder):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            if ext.lower() == '.dds':
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_folder, name + '.png' )

                try:
                    img = Image.open(input_path)
                    img.save(output_path)
                    print(f"Converted: {input_path} -> {output_path}")
                except Exception as e:
                    print(f"Error converting {input_path}: {e}")
                    
if __name__ == "__main__":
    input_folder = "gfx"
    output_folder = "gfx/converted/"

    convert_to_png(input_folder, output_folder)