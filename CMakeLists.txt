cmake_minimum_required(VERSION 3.8)
project(lanes_ros2)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(custom_msgs)
# find_package(custom_msgs REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

ament_python_install_package(${PROJECT_NAME})

# add_executable(lanes_to_cloud src/lanes_to_cloud.cpp)
# target_include_directories(lanes_to_cloud PUBLIC
#   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
#   $<INSTALL_INTERFACE:include>)

# install(TARGETS lanes_to_cloud
#   DESTINATION lib/${PROJECT_NAME})

install(PROGRAMS
  scripts/camera_geometry.py
  scripts/dummy_publisher.py
  scripts/lane_publisher.py
  scripts/lanes_to_cloud.py
  scripts/lanedetector.py
  scripts/utils/utils.py
  scripts/pcl_pub.py
  scripts/weights/yolopv2.pt
  DESTINATION lib/${PROJECT_NAME})

install(
  DIRECTORY
    images 
    launch
    scripts
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()


include_directories(
  ${PCL_INCLUDE_DIRS}
)