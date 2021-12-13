import pickle
import os


def gen_ans(annos, P):
    f = open(P, 'w')
    f.write("[\n")
    first = True
    for i in range(6):
        size = len(annos[i][0][0])          # image bb/seg cate
        for j in range(size):
            [x, y, r, d, c] = annos[i][0][0][j]
            if first:
                first = False
                f.write("   {\n")
            else:
                f.write(", \n   {\n")
            f.write("       \"image_id\": " + str(i + 1))
            f.write(", \n")

            f.write("       \"score\": " + str(c))
            f.write(", \n")

            f.write("       \"category_id\": 1")
            f.write(", \n")

            f.write("       \"bbox\": [\n")
            f.write("           " + str(x) + ", \n")
            f.write("           " + str(y) + ", \n")
            f.write("           " + str(r - x) + ", \n")
            f.write("           " + str(d - y) + "\n")
            f.write("       ], \n")

            f.write("       \"segmentation\": \n")
            st = str(annos[i][1][0][j])
            st = st.replace("b\'", "\"")
            st = st.replace("\'", "\"")

            f.write("           " + st)

            f.write("\n")
            f.write("   }")
    f.write("\n]\n")

    return


result = open('result.pkl', 'rb')

annos = pickle.load(result)


gen_ans(annos, 'answer.json')

