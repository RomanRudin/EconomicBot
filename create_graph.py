from matplotlib import pyplot as plt   


def draw_graph(max_a_for_first, max_b_for_first, max_a_for_second, max_b_for_second): 
    
    plt.title('График общей КПВ', fontsize= 25 , loc='center') 
    plt.xlabel("Товар А", fontsize=15)
    plt.ylabel("Товар Б", fontsize=15)


    plt.plot(
        [max_a_for_first, 0, 0],
        [0, max_b_for_first, max_b_for_first], "--",
        [max_a_for_second, 0, 0],
        [0, max_b_for_second, max_b_for_second], "--"
    )   


    max_a = max_a_for_first + max_a_for_second
    max_b = max_b_for_first + max_b_for_second

    max_a_between_person = max(max_a_for_first, max_a_for_second)
    max_b_between_person = max(max_b_for_first, max_b_for_second)

    plt.plot(
        [max_a, max_a_between_person, 0],
        [0, max_b_between_person, max_b]
    )


    plt.plot(
        [max_a_between_person, max_a_between_person, max_a_between_person],
        [0, 0, max_b_between_person], ":k",
        [0, 0, max_a_between_person],
        [max_b_between_person, max_b_between_person, max_b_between_person], ":k"
    )


    file_name = "photo/graph.png"
    # plt.savefig(file_name)
    plt.show()

    return file_name

draw_graph(20, 80, 60, 70)