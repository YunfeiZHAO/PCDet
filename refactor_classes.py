import os


def cut_line(line):
    line = line.split()[1:len(line.split())]
    line_result =""
    for e in line:
        line_result += " " + e
    line_result += "\n"
    return line_result

def data_refactoring(root):
    '''refact lebaling data transfered from argoverse by argoverse adapter
        https://github.com/yzhou377/argoverse-kitti-adapter
        1, replace vide file with DonCare
        2, replace labels
        :param: root of the date set dir
    '''
    for root, dirs, files in os.walk(root):
        for name in files:
            if name.endswith((".txt")):
                with open(os.path.join(root, name), "r") as f:
                    lines = f.readlines()
                if len(lines) == 0:
                    print(os.path.join(root, name))
                    # lines.append("DontCare 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n")

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
                            if line.split()[0] != "DontCare":
                                print(line)
                                print(os.path.join(root, name))
                        new_lines.append(k)
                with open(os.path.join(root, name), "w") as f:
                    f.writelines(new_lines)


def main():
    data_refactoring("./data/kitti/testing/label_2")


if __name__ == "__main__":
    main()
