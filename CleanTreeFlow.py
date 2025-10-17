import time
import xml.etree.ElementTree as ET

start_time = time.perf_counter()

def replace_char(string):
    replacements = [
        ("_x0020_", " "), ("_x0026_","&"), ("_x0027_","'"), ("_x0028_", "("), ("_x0029_", ")"), 
        ("_x0030_", "0"), ("_x0031_", "1"), ("_x0032_", "2"), ("_x0033_", "3"), ("_x0034_", "4"), 
        ("_x0035_", "5"), ("_x0036_", "6"), ("_x0037_", "7"), ("_x0038_", "8"), ("_x0039_", "9"), 
        ("_x002b_","+")]
    for old, new in replacements:
        string = string.replace(old, new)
    return string

def get_tags(root):
    tags = []
    for node in root.findall('service-providers'):
        for subchild in node:
            for subsubchild in subchild:
                for subsubsubchild in subsubchild:
                    tags.append(subchild.tag)
                    tags.append(subsubchild.tag)
                    tags.append(subsubsubchild.tag)
                    break
    return tags

def main():
    #open and parse xml file, replace ".content.xml" with the path of the file if is necessary
    tree = ET.parse('.content.xml')
    root = tree.getroot()


    #Extract and print tags
    tags = get_tags(root)
    modified_tags = [replace_char(tag) for tag in tags]
    for i in range(0, len(modified_tags), 3):
        print(" ".join(modified_tags[i:i+3]))

if __name__ == "__main__":
    main()

#End time
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"\nElapse time: {elapsed_time:.2f} seconds")