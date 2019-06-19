cd ~/mjpg-streamer-master/mjpg-streamer-experimental
./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -p 8083 -w ./www"
python3 ~/Document/car_test/sender.py
python ~/Document/car_test/control.py