#include <kipr/botball.h>

int main()
{
    create_connect();
    enable_servos();
    set_servo_position(2,1600);
    msleep(1000);
    set_servo_position(1,122);
    msleep(1000);
    set_create_total_angle(0);
    int i = 0;
    while (analog(1)<1000){
        create_drive_direct(45,50);
    }
    create_drive_direct(45,50);
    msleep(2800);

    while (analog(1)<1000){
        create_drive_direct(-50, 50);
        msleep(10);
    }


    while(i<3768)
    {
        if (analog(1)<1000){
            create_drive_direct(25,50);
            i = i + 1;
        }
        else{
            create_drive_direct(50,25);
            i = i + 1;
        }
    }
    while (get_create_total_angle() > 9){
      create_drive_direct(50, -50);
      msleep(3);
    }
    create_drive_direct(-50,-50);
    msleep(1560);
    create_stop();
    msleep(300);
    set_servo_position(1,1600);
    msleep(1000);
    set_servo_position(2,600);
    msleep(1000);
    set_servo_position(1,1113);
    msleep(1000);
    return 0;
}