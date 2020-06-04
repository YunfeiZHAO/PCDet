import os
import random

def cut_line(line):
    line = line.split()[1:len(line.split())]
    line_result =""
    for e in line:
        line_result += " " + e
    line_result += "\n"
    return line_result

def data_refactoring(root_dir):
    '''refact lebaling data transfered from argoverse by argoverse adapter
        https://github.com/yzhou377/argoverse-kitti-adapter
        1, replace empty file with DonCare
        2, replace labels
        :param: root of the date set dir
    '''
    os.system(f"""rm -f {os.path.join(root_dir, 'ImageSets/val.txt')}""")
    os.system(f"""rm -f {os.path.join(root_dir, 'ImageSets/train.txt')}""")
    os.system(f"""rm -f {os.path.join(root_dir, 'ImageSets/test.txt')}""")
    random.seed(1)
    test = []
    validation = []
    train = []
    for root, dirs, files in os.walk("./data/kitti/testing/label_2"):
        for name in files:
            if name.endswith((".txt")):
                empty = True
                with open(os.path.join(root, name), "r") as f:
                    lines = f.readlines()
                if len(lines) == 0:
                    print(os.path.join(root, name))
                else:
                    new_lines = []
                    for line in lines:
                        if line.split()[0] == "VEHICLE":
                            k = "Car"+cut_line(line)
                        elif line.split()[0] == "PEDESTRIAN":
                            k = "Pedestrian"+cut_line(line)
                        elif line.split()[0] == "ON_ROAD_OBSTACLE":
                            k = "DontCare"+cut_line(line)
                        elif line.split()[0] == "LARGE_VEHICLE":
                            k = "Van"+cut_line(line)
                        elif line.split()[0] == "BICYCLE":
                            k = "Cyclist"+cut_line(line)
                        elif line.split()[0] == "BICYCLIST":
                            k = "Cyclist"+cut_line(line)
                        elif line.split()[0] == "BUS":
                            k = "Truck"+cut_line(line)
                        elif line.split()[0] == "OTHER_MOVER":
                            k = "Misc"+cut_line(line)
                        elif line.split()[0] == "TRAILER":
                            k = "Misc"+cut_line(line)
                        elif line.split()[0] == "MOTORCYCLIST":
                            k = "Cyclist"+cut_line(line)
                        elif line.split()[0] == "MOPED":
                            k = "Cyclist"+cut_line(line)
                        elif line.split()[0] == "MOTORCYCLE":
                            k = "Cyclist"+str(line.split()[1:len(line.split())-1] )
                        elif line.split()[0] == "STROLLER":
                            k = "Pedestrian"+cut_line(line)
                        elif line.split()[0] == "EMERGENCY_VEHICLE":
                            k = "Van"+cut_line(line)
                        elif line.split()[0] == "ANIMAL":
                            k = "Misc"+cut_line(line)
                        else:
                            k = line
                        k = k.strip()
                        k = k.strip('\n')
                        k_a = k.split(' ')
                        if (len(k_a) != 15):
                            print("Irregular length:", len(k_a))
                            print(k)
                        if k_a[0] != "DontCare":
                            empty = False
                            new_lines.append(k + '\n')
                os.system(f"rm {os.path.join(root, name)}")
                if not empty:
                    filename = name.strip(".txt")
                    filename = filename + '\n'
                    if random.random() <=0.7:
                        train.append(filename)
                    else:
                        validation.append(filename)
                    test.append(filename)
                    with open(os.path.join(root, name), "w") as f:
                        f.writelines(new_lines)
    with open(os.path.join(root_dir, f'ImageSets/train.txt'), "w") as f:
        f.writelines(train)
    with open(os.path.join(root_dir, f'ImageSets/val.txt'), "w") as f:
        f.writelines(validation)
    with open(os.path.join(root_dir, f'ImageSets/test.txt'), "w") as f:
        f.writelines(test)
    print(f'train size: {len(train)}')
    print(f'validation size: {len(validation)}')
    print(f'test size: {len(test)}')

def main():
    data_refactoring("./data/kitti")


if __name__ == "__main__":
    main()
