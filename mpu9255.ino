#include <Wire.h>
#include <MPU925X.h>
MPU925X mpu;
void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  // Initialize MPU925X
  while (!mpu.begin(MPU925X_GYRO_RANGE_250DPS, MPU925X_ACCEL_RANGE_2G, MPU925X_SAMPLE_RATE_DIV_1000)) {
    Serial.println("MPU925X connection failed. Please check your connections.");
    delay(5000);
  }
  Serial.println("MPU925X initialized successfully!");
}
void loop() {
  // Read accelerometer and gyroscope data
  float ax, ay, az;
  float gx, gy, gz;
  mpu.readAccelData(&ax, &ay, &az);
  mpu.readGyroData(&gx, &gy, &gz);

  Serial.print("Accel (m/s^2): ");
  Serial.print("X = "); Serial.print(ax); Serial.print(", ");
  Serial.print("Y = "); Serial.print(ay); Serial.print(", ");
  Serial.print("Z = "); Serial.println(az);

  Serial.print("Gyro (°/s): ");
  Serial.print("X = "); Serial.print(gx); Serial.print(", ");
  Serial.print("Y = "); Serial.print(gy); Serial.print(", ");
  Serial.print("Z = "); Serial.println(gz);

  delay(1000);  // Delay for 1 second
}
