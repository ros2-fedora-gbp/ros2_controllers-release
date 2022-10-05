%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2-controllers
Version:        2.13.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_controllers package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-diff-drive-controller
Requires:       ros-rolling-effort-controllers
Requires:       ros-rolling-force-torque-sensor-broadcaster
Requires:       ros-rolling-forward-command-controller
Requires:       ros-rolling-imu-sensor-broadcaster
Requires:       ros-rolling-joint-state-broadcaster
Requires:       ros-rolling-joint-trajectory-controller
Requires:       ros-rolling-position-controllers
Requires:       ros-rolling-tricycle-controller
Requires:       ros-rolling-velocity-controllers
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Metapackage for ROS2 controllers related packages

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Oct 05 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.13.0-1
- Autogenerated by Bloom

* Thu Sep 01 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.0-1
- Autogenerated by Bloom

* Thu Aug 04 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.11.0-1
- Autogenerated by Bloom

* Mon Aug 01 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.10.0-1
- Autogenerated by Bloom

* Thu Jul 14 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.9.0-1
- Autogenerated by Bloom

* Sat Jul 09 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.8.0-1
- Autogenerated by Bloom

* Sun Jul 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.7.0-1
- Autogenerated by Bloom

* Sat Jun 18 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.6.0-1
- Autogenerated by Bloom

* Fri May 13 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.5.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.4.0-1
- Autogenerated by Bloom

* Thu Apr 21 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.3.0-1
- Autogenerated by Bloom

* Fri Mar 25 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.2.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.0.1-2
- Autogenerated by Bloom

