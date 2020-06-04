from pcdet.utils.object3d_utils import Object3d

import pickle
import numpy as np
import cv2
import os


class Visualisation:
    # show result of the pkl file
    def __init__(self, result_folder_path, image_folder_path, image_idx):
        self.image_dir = image_folder_path
        self.result_dir = result_folder_path
        self.Objects3d = self.get_Object3d(image_idx)
        self.img = self.get_image(image_idx)

    def get_image(self, idx):
        img_filename = os.path.join(self.image_dir, "%06d.png" % (idx))
        return cv2.imread(img_filename)

    def get_Object3d(self, idx):
        Objects3d = []
        result_filename = os.path.join(self.result_dir, "%06d.txt" % (idx))
        with open(result_filename) as fp:
            Lines = fp.readlines()
            for line in Lines:
                Objects3d.append(Object3d(line))
        return Objects3d

    #, calib, show3d = True, depth = None

    def show_image_with_2Dboxes(self, img):
        """ Show image with 2D bounding boxes """
        img1 = np.copy(img)  # for 2d bbox
        img2 = np.copy(img)  # for 3d bbox
        for obj in self.Objects3d:
            if obj.cls_type == "DontCare":
                continue
            cv2.rectangle(
                img1,
                (int(obj.box2d[0]), int(obj.box2d[1])),
                (int(obj.box2d[2]), int(obj.box2d[3])),
                (0, 255, 0),
                2,
            )
        cv2.imshow("2dbox", img1)


    def show_image_with_3Dboxes(self, img):
        """ Show image with 3D bounding boxes """
        generate_corners3d

            # box3d_pts_2d, box3d_pts_3d = utils.compute_box_3d(obj, calib.P)
            # img2 = utils.draw_projected_box3d(img2, box3d_pts_2d)

            # project
            # box3d_pts_3d_velo = calib.project_rect_to_velo(box3d_pts_3d)
            # box3d_pts_32d = utils.box3d_to_rgb_box00(box3d_pts_3d_velo)
            # box3d_pts_32d = calib.project_velo_to_image(box3d_pts_3d_velo)
            # img3 = utils.draw_projected_box3d(img3, box3d_pts_32d)
        # print("img1:", img1.shape)
        cv2.imshow("2dbox", img1)
        # print("img3:",img3.shape)
        # Image.fromarray(img3).show()
        # show3d = True
        # if show3d:
        #     # print("img2:",img2.shape)
        #     cv2.imshow("3dbox", img2)
        # if depth is not None:
        #     cv2.imshow("depth", depth)

def main():
    V = Visualisation('/home/yunfei/Desktop/PCDet/data/kitti/training/label_2', '/home/yunfei/Desktop/PCDet/data/kitti/training/image_2', 1)
    V.show_image_with_boxes(V.img)
    cv2.waitKey()
if __name__ == '__main__':
    main()