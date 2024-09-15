"""
Файл с функцией, которая создает график общей КПВ при заданных значениях
"""

from matplotlib import pyplot as plt


def draw_graph(max_a_for_first: int, max_b_for_first: int,
               max_a_for_second: int, max_b_for_second: int) -> str:
    """ создает график общей КПВ при заданных значениях """

    plt.title('График общей КПВ', fontsize= 25 , loc='center')
    plt.xlabel("Товар А", fontsize=15)
    plt.ylabel("Товар Б", fontsize=15)

    axes = plt.gca()

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


    polygon_1 = plt.Polygon(
        [(0, max_b),
        (max_a_between_person, max_b_between_person),
        (0, max_b_between_person)],
        color="b",
        alpha=0.25,
    )
    polygon_2 = plt.Polygon(
        [(max_a, 0),
        (max_a_between_person, max_b_between_person),
        (max_a_between_person, 0)],
        color="r",
        alpha=0.25,
    )

    axes.add_patch(polygon_1)
    axes.add_patch(polygon_2)

    file_name = "photo\\graph.png"
    plt.savefig(file_name)

    plt.close()

    return file_name
