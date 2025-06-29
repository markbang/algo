import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.action_chains import ActionChains


def hanta(n, A, B, C):
    if n == 1:
        move(A, C)
    else:
        hanta(n - 1, A, C, B)
        move(A, C)
        hanta(n - 1, B, A, C)


def move(src, dest):
    # 获取 canvas 元素
    canvas = driver.find_element("id", "canvas")
    # 获取 canvas 元素在页面上的位置
    canvas_location = canvas.location
    # 获取目标位置
    src_x, src_y = dest_locations[src]

    dest_x, dest_y = dest_locations[dest]
    # 计算鼠标相对于页面的绝对位置
    absolute_x = canvas_location["x"] + dest_x
    absolute_y = canvas_location["y"] + dest_y
    # 在目标位置模拟鼠标点击
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(
        canvas, absolute_x, absolute_y
    ).click().perform()
    time.sleep(0.5)  # 添加延迟以便更好地观察


def play(n):
    global driver
    driver = webdriver.Chrome()
    try:
        driver.get("https://zhangxiaoleiwk.gitee.io/h.html")
        driver.find_element("id", "bt_run").click()
        driver.find_element("id", "input_floor").send_keys(str(n))
        time.sleep(1)  # 等待页面响应
        hanta(n, "A", "B", "C")
    finally:
        driver.quit()


# 每个位置的坐标，根据实际情况调整
dest_locations = {
    "A": (100, 300),  # 示例中的 A 的位置坐标
    "B": (300, 300),  # 示例中的 B 的位置坐标
    "C": (500, 300),  # 示例中的 C 的位置坐标
}

if __name__ == "__main__":
    play(10)
