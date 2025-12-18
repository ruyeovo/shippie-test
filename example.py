@Override
    public void setActivityController(IActivityController controller, boolean imAMonkey) {
        mAmInternal.enforceCallingPermission(android.Manifest.permission.SET_ACTIVITY_WATCHER,
                "setActivityController()");
        synchronized (mGlobalLock) {
            mController = controller;
            mControllerIsAMonkey = imAMonkey;

            if (mControllerIsAMonkey) {
                mTrueTime = format.format(new Date());
                Slog.d(TAG, "setActivityController imAMonkey is true, "
                        + "calling pid = " + Binder.getCallingPid()
                        + ", calling uid = " + Binder.getCallingUid()
                        + ", callstack = " + Log.getStackTraceString(new Throwable()));
            } else {
                mFalseTime = format.format(new Date());
                Slog.d(TAG, "setActivityController imAMonkey is false, "
                        + "calling pid = " + Binder.getCallingPid()
                        + ", calling uid = " + Binder.getCallingUid()
                        + ", callstack = " + Log.getStackTraceString(new Throwable()));
            }

            Watchdog.getInstance().setActivityController(controller);
        }
    }