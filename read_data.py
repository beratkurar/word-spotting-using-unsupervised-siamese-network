import cv2
import h5py

if __name__ == "__main__":
    f1 = h5py.File("fold1.hdf5", "r")
    fold1 = {'train': list(zip(f1['train_left_images'], f1['train_right_images'], f1['train_labels'])),
             'test': list(zip(f1['test_left_images'], f1['test_right_images'], f1['test_labels'])),
             'validations': list(zip(f1['validation_left_images'], f1['validation_right_images'], f1['validation_labels']))}

    f2 = h5py.File("fold2.hdf5", "r")
    fold2 = {'train': list(zip(f2['train_left_images'], f2['train_right_images'], f2['train_labels'])),
             'test': list(zip(f2['test_left_images'], f2['test_right_images'], f2['test_labels'])),
             'validations': list(zip(f2['validation_left_images'], f2['validation_right_images'], f2['validation_labels']))}

    f3 = h5py.File("fold3.hdf5", "r")
    fold3 = {'train': list(zip(f3['train_left_images'], f3['train_right_images'], f3['train_labels'])),
             'test': list(zip(f3['test_left_images'], f3['test_right_images'], f3['test_labels'])),
             'validations': list(zip(f3['validation_left_images'], f3['validation_right_images'], f3['validation_labels']))}


    # Example: read the i'th example from train set in fold 1

    set_ref = 'train'  # train/test/validation
    example_idx = 120  # index of the example
    first_img = fold1[set_ref][example_idx][0]  # first patch
    second_img = fold1[set_ref][example_idx][1]  # second patch
    label = fold1[set_ref][example_idx][2]  # example's label. 1 if the first is to left of the second and -1 otherwise

    cv2.imshow('left', first_img)
    cv2.imshow('right', second_img)
    print('label: ', label)
    cv2.waitKey(0)
