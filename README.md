# eye_examination
Examine your eyes and get the best distance to watch your screen.检查您的眼睛并得到您观看屏幕的最佳距离。
# eye.py
Run directly and then a window will appear.You can press 'w','a','s','d' or click the side of the window to tell the computer which direction the 'E' in the middle of the window is facing to.The score will be shown after you press 'Esc' to break the window.Press '1' to '9' and '0' can change the size of 'E' from 1 to 10,the size means the thickness of 'E'(pixels).You can change the colors by modifying the code.
直接运行，会出现一个窗口。你可以按'w','a','s','d'或者点击窗口的侧面告诉计算机窗口中间的'E'正对着哪个方向。按'Esc'打破窗口后会显示分数。按'1'到'9'，'0'可以改变'E'的大小从1到10，大小表示'E'的粗细（像素）。你可以通过修改代码来改变颜色。
# draw_Es.py
Run directly and you will get eye.png,its size is 1080x1080.Most screen has a width of 1080 pixels.
直接运行你将得到eye.png，它的尺寸1080x1080。大多数屏幕的宽度都是1080像素。
# caculation 计算
Eyesight is 1.0 means you can distinguish 1' angle of vision.If your eyesight is 1.0 and your screen is 15.6 inches with 1920x1080 pixels,you can see every pixels of the screen clearly at a distance of 62 cm.The formula is below:
diameter_of_pixel(mm)=screeninches/(pixelsX^2+pixelsY^2)^0.5\*25.4
eyesight=diameter_of_pixel(mm)\*Esize/distance(mm)\*10800/pi
视力为1.0表示您可以分辨1'的视角。如果您的视力为1.0，屏幕为15.6英寸，1920x1080像素，则在62厘米的距离处您可以清楚地看到屏幕的每个像素。公式如下：
像素直径（毫米）=屏幕尺寸（英寸）/(X方向像素^2+Y方向像素^2)^0.5\*25.4
视力=像素直径（毫米）\*Esize/距离（毫米）\*10800/圆周率
