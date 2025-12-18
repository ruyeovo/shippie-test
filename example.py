@Override
    public void setActivityController(IActivityController controller, boolean imAMonkey) {
        mAmInternal.enforceCallingPermission(android.Manifest.permission.SET_ACTIVITY_WATCHER,
                "setActivityController()");
        synchronized (mGlobalLock) {
            mController = controller;
            mControllerIsAMonkey = imAMonkey;
            Watchdog.getInstance().setActivityController(controller);
        }
    }