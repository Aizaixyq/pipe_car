#include <opencv2/opencv.hpp>
//#include <fmt/core.h>

int main()
{
    cv::VideoCapture cap("http://192.168.3.18:8081");
 
    //capture.open("1.avi"); //打开视频文件
    //cap.open("http://192.168.3.18:8081");
 
    //创建VideoCapture对象的另一种方式
    //VideoCapture capture("rtsp://admin:hikvision2021@192.168.1.64");
    if (!cap.isOpened()) {
        //fmt::print("ERROR! Unable to open camera\n");
        return 1;
    }
 
    cv::Mat frame;
 
    while (1)
    {
        cap.read(frame);
        // check if we succeeded
        if (frame.empty()) {
            //fmt::print("ERROR! blank frame grabbed\n");
            break;
        }
        imshow("test", frame);
        if(cv::waitKey(1) == 'q')
            break;
    }
 
    cv::destroyWindow("test");
    cap.release();//必须加release释放，否则会内存泄漏
 
    return 0;
}