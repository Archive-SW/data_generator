import imgaug.augmenters as iaa
import imgaug as ia
import cv2
import os, sys

class DataAugmentation():
    def __init__(self):
        self.path = sys.argv[1]
    
    def load_images_from_folder(self, folder):
        images = []
        img_filename = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                images.append(img)
                img_filename.append(filename)
            print("image loded ",str(filename))
        return images, img_filename

    def write_images(self, images, aug_img_path, img_filename, num):
        for i in range(0,len(images)):
            img_filename_str = img_filename[i].split(".png")
            cv2.imwrite(aug_img_path+img_filename_str[0]+"_"+str(num)+".png", images[i])
        print("image saving complete")
        
    def augmentations(self, images):       
        seq1 = iaa.Sequential([
            iaa.AverageBlur(k=(2,7)),
            iaa.MedianBlur(k = (3,7))
        ])
        seq2 = iaa.ChannelShuffle(p=1.0)
        seq3 = iaa.Dropout((0.05, 0.1), per_channel=0.5)
        seq4 = iaa.Sequential([
            iaa.Add((-15,15)),
            iaa.Multiply((0.3, 1.5))
        ])
        seq5 = iaa.Sequential([
            iaa.Crop(px=(0, 60)), # crop images from each side by 0 to 16px (randomly chosen)
            iaa.GaussianBlur(sigma=(0, 1.5)) # blur images with a sigma of 0 to 3.0
        ])

        print("image augmentation beginning")
        img1=seq1.augment_images(images)
        print("sequence 1 completed......")
        img2=seq2.augment_images(images)
        print("sequence 2 completed......")
        img3=seq3.augment_images(images)
        print("sequence 3 completed......")
        img4=seq4.augment_images(images)
        print("sequence 4 completed......")
        img5=seq5.augment_images(images)
        print("sequence 5 completed......")
        print("proceed to next augmentations")
        list = [img1, img2, img3, img4, img5]
        return list
                                                      


def main():
    da = DataAugmentation()
    photos1, photos1_filename = da.load_images_from_folder(os.path.join(da.path))
    photo_augmented = da.augmentations(photos1)
    for num in range(0, 5):
        da.write_images(photo_augmented[num], da.path, photos1_filename, num)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ')
        exit('$ python data_augmentation.py your_data_path')

    main()