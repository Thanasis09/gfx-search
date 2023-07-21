import os

def generate_entry(output_file, gfx_folder):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for root, _, filenames in os.walk(gfx_folder):
                for filename in filenames:
                    folder_name = os.path.basename(root)
                    icon_name = os.path.splitext(filename)[0]
                    icon_path = os.path.join(root, filename).replace(os.path.sep, '/')
                    
                    entry = (
                        f'<div data-clipboard-text="{icon_name}" data-search-text="{icon_name}" '
                        f'title="{icon_name}" class="{folder_name}">\n'
                        f'    <img src="{icon_path}" alt="{icon_name}">\n'
                        f'</div>\n'
                    )
                    f.write(entry)
            print(f"Generation complete! Entries saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
                
                


if __name__ =="__main__":
    gfx_folder = "gfx"
    output_file = "gfx_entries.html"
    
    generate_entry(output_file, gfx_folder)