import torch


def rot90(image):
    '''
    Rotate an image by 90 degree by first transposing the image and then flipping it vertically.

    :param image: The image that should be rotated.
    :return: The rotated image.
    '''

    # transpose
    trans_im = image.permute(0, 2, 1)

    # flip vertically
    flip_idx = torch.range(trans_im.size(2) - 1, 0, -1).long()
    rot_im = trans_im.index_select(2, flip_idx)

    return  rot_im


def rot180(image):
    '''
    Rotate an image by 180 degree by first flipping the image vertically and then horizontally.

    :param image: The image that should be rotated.
    :return: The rotated image.
    '''

    # flip vertically
    vert_idx = torch.range(image.size(2) - 1, 0, -1).long()
    vert_im = image.index_select(2, vert_idx)

    # flip horizontally
    hor_idx = torch.range(vert_im.size(1) - 1, 0, -1).long()
    rot_im = vert_im.index_select(1, hor_idx)

    return rot_im


def rot270(image):
    '''
    Rotate an image by 270 degree by first flipping the image vertically and then transposing it.

    :param image: The image that should be rotated.
    :return: The rotated image
    '''

    # flip vertically
    vert_idx = torch.range(image.size(2) - 1, 0, -1).long()
    vert_im = image.index_select(2, vert_idx)

    # transpose
    rot_im = vert_im.permute(0, 2, 1)

    return rot_im


def apply(func, M):
    '''
    Applies a function on valid arguments or list of arguments.

    :param func: The function that we want to apply.
    :param M: The argument or list of arguments that will be passed to the function.
    :return: The result that the function returns.
    '''

    tList = [func(m) for m in torch.unbind(M, dim=0)]
    res = torch.stack(tList, dim=0)

    return res