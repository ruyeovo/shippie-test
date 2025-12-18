@Override
    public void setActivityController(IActivityController controller, boolean imAMonkey) {
        mAmInternal.enforceCallingPermission(android.Manifest.permission.SET_ACTIVITY_WATCHER,
                "setActivityController()");
        synchronized (mGlobalLock) {
            mController = controller;
            mControllerIsAMonkey = imAMonkey;
            if (controller != null && imAMonkey &&
                    ("1".equals(SystemProperties.get("persist.sys.audio.premonkeycontrl", "0")))) {
                SystemProperties.set("sys.audio.monkeycontrl", "1");
                if (null != mContext) {
                    AudioManager audioManager = (AudioManager) mContext.getSystemService(Context.AUDIO_SERVICE);
                    if (null != audioManager) {
                        audioManager.setParameters("fm_radio_mute=1");
                        Log.i(TAG, "fm_radio_mute=1");
                    }
                }
            }

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