from manim import *
import numpy as np

class ElegantStackAnimation4K(Scene):
    def construct(self):
        # 4K分辨率配置
        self.apply_4k_config()
        
        # 标题
        title = Text("Stack | 栈", font_size=54, color=BLUE)
        title.to_edge(UP)
        
        # 副标题
        subtitle = Text("LIFO - 后进先出", font_size=28, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle))
        self.wait(1)
        
        # 创建栈框架
        stack_frame = self.create_4k_stack_frame()
        
        # 创建栈元素
        stack_elements = VGroup()
        
        # 操作说明
        operations_text = Text("操作:", font_size=26, color=WHITE)
        operations_text.to_edge(DOWN).to_edge(LEFT)
        
        self.play(
            Create(stack_frame),
            Write(operations_text)
        )
        
        # 初始元素
        elements_data = [
            ("Data A", BLUE),
            ("Data B", GREEN), 
            ("Data C", YELLOW),
            ("Data D", RED)
        ]
        
        # 添加初始元素到栈
        for i, (char, color) in enumerate(elements_data):
            element = self.create_4k_stack_element(char, color)
            element.move_to(stack_frame.get_bottom() + UP * (i * 0.8 + 0.4))
            stack_elements.add(element)
            
            self.play(
                element.animate.move_to(stack_frame.get_bottom() + UP * (i * 0.8 + 0.4)),
                run_time=0.6
            )
        
        self.wait(1)
        
        # 显示栈指针
        stack_pointer = self.create_4k_stack_pointer(stack_frame, len(stack_elements))
        self.play(Create(stack_pointer))
        
        # 操作演示
        self.demo_4k_operations(stack_frame, stack_elements, stack_pointer, operations_text)
    
    def apply_4k_config(self):
        """应用4K配置"""
        try:
            config.pixel_height = 2160
            config.pixel_width = 3840
            config.frame_rate = 60
        except:
            pass  # 如果配置失败，使用命令行参数
    
    def create_4k_stack_frame(self):
        """4K分辨率下的精细栈框架"""
        frame = Rectangle(
            width=2.5,
            height=5,
            stroke_color=WHITE,
            stroke_width=2.5,
            fill_color=BLACK,
            fill_opacity=0.85
        )
        frame.to_edge(LEFT, buff=3)
        
        # 底部线条
        bottom_line = Line(
            frame.get_corner(DL),
            frame.get_corner(DR),
            stroke_width=3,
            color=WHITE
        )
        
        return VGroup(frame, bottom_line)
    
    def create_4k_stack_element(self, text, color):
        """4K分辨率下的精细栈元素"""
        element = RoundedRectangle(
            width=2.3,
            height=0.7,
            corner_radius=0.1,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        text_obj = Text(text, font_size=22, color=WHITE)
        text_obj.move_to(element.get_center())
        
        return VGroup(element, text_obj)
    
    def create_4k_stack_pointer(self, stack_frame, element_count):
        """4K分辨率下的精细栈指针"""
        pointer = Arrow(
            start=stack_frame.get_right() + RIGHT * 0.8,
            end=stack_frame.get_right() + RIGHT * 0.1,
            buff=0,
            stroke_color=YELLOW,
            stroke_width=5,
            tip_length=0.2
        )
        
        pointer_label = Text("SP", font_size=20, color=YELLOW)
        pointer_label.next_to(pointer, RIGHT, buff=0.15)
        
        top_position = stack_frame.get_bottom() + UP * (element_count * 0.8)
        pointer_group = VGroup(pointer, pointer_label)
        pointer_group.move_to(top_position + RIGHT * 1.5)
        
        return pointer_group
    
    def demo_4k_operations(self, stack_frame, stack_elements, stack_pointer, operations_text):
        """4K分辨率下的操作演示"""
        
        # 使用Text显示代码而不是Code类
        code_text = self.create_code_text(
            "std::stack<std::string> s;\n\n"
            "// 压栈操作\n"
            "s.push(\"New Data\");"
        )
        code_text.to_edge(RIGHT, buff=1)
        
        self.play(Write(code_text))
        
        # 压栈操作
        push_text = Text("push('New Data')", font_size=26, color=GREEN)
        push_text.next_to(operations_text, RIGHT)
        
        self.play(Write(push_text))
        
        # 创建新元素
        new_element = self.create_4k_stack_element("New Data", PURPLE)
        new_element.move_to(stack_frame.get_bottom() + DOWN * 0.8)
        
        self.play(Create(new_element))
        
        # 移动到栈顶
        target_position = stack_frame.get_bottom() + UP * (len(stack_elements) * 0.8 + 0.4)
        
        self.play(
            new_element.animate.move_to(target_position),
            stack_pointer.animate.move_to(target_position + RIGHT * 1.5),
            run_time=1.2
        )
        
        stack_elements.add(new_element)
        self.wait(1)
        
        # 更新代码显示
        updated_code = self.create_code_text(
            "// 查看栈顶\n"
            "string top = s.top();\n"
            "// top = \"New Data\"\n\n"
            "// 弹栈操作\n"
            "s.pop();"
        )
        updated_code.to_edge(RIGHT, buff=1)
        
        self.play(Transform(code_text, updated_code))
        self.play(FadeOut(push_text))
        
        # 弹栈操作
        pop_text = Text("pop() → 'New Data'", font_size=26, color=RED)
        pop_text.next_to(operations_text, RIGHT)
        
        self.play(Write(pop_text))
        
        # 高亮要弹出的元素
        self.play(
            stack_elements[-1].animate.set_stroke_color(RED).set_stroke_width(4),
            run_time=0.5
        )
        
        # 移动指针
        if len(stack_elements) > 1:
            new_pointer_pos = stack_frame.get_bottom() + UP * ((len(stack_elements)-1) * 0.8) + RIGHT * 1.5
        else:
            new_pointer_pos = stack_frame.get_bottom() + RIGHT * 1.5
        
        self.play(
            stack_pointer.animate.move_to(new_pointer_pos),
            run_time=0.5
        )
        
        # 移除元素
        removed_element = stack_elements[-1]
        self.play(
            removed_element.animate.move_to(stack_frame.get_right() + RIGHT * 3),
            run_time=1
        )
        
        self.play(FadeOut(removed_element))
        stack_elements.remove(removed_element)
        
        self.wait(1)
        self.play(FadeOut(pop_text))
        
        # 最终展示
        final_text = Text("4K栈动画演示完成!", font_size=42, color=GREEN)
        final_text.move_to(ORIGIN)
        
        self.play(Write(final_text))
        self.wait(2)
    
    def create_code_text(self, code_str):
        """创建代码样式的文本（兼容不同Manim版本）"""
        lines = code_str.split('\n')
        code_group = VGroup()
        
        for i, line in enumerate(lines):
            if '//' in line:
                # 注释行
                parts = line.split('//')
                main_text = Text(parts[0], font_size=18, color=WHITE, font="Monospace")
                comment_text = Text("//" + parts[1], font_size=18, color=GRAY, font="Monospace")
                comment_text.next_to(main_text, RIGHT, buff=0.1)
                line_group = VGroup(main_text, comment_text)
            else:
                # 代码行
                line_group = Text(line, font_size=18, color=WHITE, font="Monospace")
            
            line_group.shift(DOWN * i * 0.5)
            code_group.add(line_group)
        
        return code_group

class CppSTLStackDemo4K(Scene):
    """C++ STL 栈用法演示 - 4K版本"""
    
    def construct(self):
        # 4K配置
        self.apply_4k_config()
        
        title = Text("C++ STL stack 用法 - 4K演示", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 包含头文件
        include_code = self.create_code_text("#include <stack>\n#include <iostream>")
        include_code.to_edge(UP).shift(DOWN * 1.5)
        
        self.play(Write(include_code))
        self.wait(1)
        
        # 创建栈
        create_code = self.create_code_text("std::stack<int> s;  // 创建整型栈")
        create_code.next_to(include_code, DOWN, buff=0.8)
        
        self.play(Write(create_code))
        self.wait(1)
        
        # 操作演示
        operations = [
            "s.push(10);     // 压栈",
            "s.push(20);",
            "s.push(30);",
            "int top = s.top();  // 查看栈顶 → 30",
            "s.pop();        // 弹栈",
            "bool empty = s.empty();  // 判断空栈",
            "int size = s.size();     // 获取大小"
        ]
        
        current_y = create_code.get_bottom()[1] - 1
        code_objects = []
        
        for i, operation in enumerate(operations):
            code_obj = self.create_code_text(operation)
            code_obj.move_to([1, current_y - i * 0.6, 0])
            code_objects.append(code_obj)
            
            self.play(Write(code_obj), run_time=0.5)
            self.wait(0.3)
        
        self.wait(2)
        
        # 完整示例
        full_example = Text("完整示例:", font_size=32, color=YELLOW)
        full_example.next_to(code_objects[-1], DOWN, buff=1.2)
        self.play(Write(full_example))
        
        complete_code = self.create_multiline_code("""
#include <stack>
#include <iostream>

int main() {
    std::stack<int> s;
    
    s.push(1);
    s.push(2); 
    s.push(3);
    
    while (!s.empty()) {
        std::cout << s.top() << " ";
        s.pop();
    }
    // 输出: 3 2 1
    return 0;
}""")
        complete_code.next_to(full_example, DOWN, buff=0.8)
        
        self.play(Write(complete_code))
        self.wait(3)
    
    def apply_4k_config(self):
        """应用4K配置"""
        try:
            config.pixel_height = 2160
            config.pixel_width = 3840
            config.frame_rate = 60
        except:
            pass
    
    def create_code_text(self, code_str):
        """创建代码文本"""
        if '//' in code_str:
            parts = code_str.split('//')
            main_text = Text(parts[0], font_size=20, color=WHITE, font="Monospace")
            comment_text = Text("//" + parts[1], font_size=20, color=GRAY, font="Monospace")
            comment_text.next_to(main_text, RIGHT, buff=0.1)
            return VGroup(main_text, comment_text)
        else:
            return Text(code_str, font_size=20, color=WHITE, font="Monospace")
    
    def create_multiline_code(self, code_str):
        """创建多行代码"""
        lines = code_str.strip().split('\n')
        code_group = VGroup()
        
        for i, line in enumerate(lines):
            if line.strip().startswith('//'):
                text = Text(line, font_size=16, color=GRAY, font="Monospace")
            else:
                text = Text(line, font_size=16, color=WHITE, font="Monospace")
            text.shift(DOWN * i * 0.4)
            code_group.add(text)
        
        return code_group

# 运行命令
if __name__ == "__main__":
    import os
    print("渲染4K栈动画:")
    print("manim -pql -qk scene.py ElegantStackAnimation4K")
    print("manim -pql -qk scene.py CppSTLStackDemo4K")