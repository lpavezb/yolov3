from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def accuracy_and_distance():
    with open("test/list.txt") as test:
        with open("digits_results.txt") as results:
            test_dict = dict(map(lambda line: line.replace("\n", "").split("\t"), test.readlines()))
            results_dict = dict(map(lambda line: line.replace("\n", "").split("\t"), results.readlines()))
            test_dict.pop("handwritten_MX8900201931130441127_RcZzCL7K3kWpxc-qgqhAcw.bmp")
            test_dict.pop("handwritten_MX8900201931130648335_rY70W7K-FE2QCWZS4SefUQ.bmp")
            results_dict.pop("handwritten_MX8900201931130441127_RcZzCL7K3kWpxc-qgqhAcw.bmp")
            results_dict.pop("handwritten_MX8900201931130648335_rY70W7K-FE2QCWZS4SefUQ.bmp")

            total = 0
            acc = 0
            s_distance = 0
            for key in test_dict:
                total += 1
                predicted = results_dict[key]
                real = test_dict[key]
                acc += predicted == real
                similarity = similar(predicted, real)
                if similarity < 0.35:
                     print(f"image {key}, silimarity {similarity}. Predicted: {predicted}. Real: {real}")
                s_distance += similarity

            print(f"accuracy: {acc / total}")
            print(f"distance: {s_distance / total}")


def get_number(path, pred):
    bsl = path[::-1].find("/")
    img_name = path[len(path) - bsl:]
    if pred[0] is not None:
        l = pred[0].tolist()
        l.sort(key=lambda x: x[0])
        res = ""
        for n in l:
            res += str(int(n[-1]))
        return img_name + "\t" + res
    else:
        return img_name + "\t"


if __name__ == '__main__':
	accuracy_and_distance()