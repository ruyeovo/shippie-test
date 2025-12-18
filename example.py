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
            Watchdog.getInstance().setActivityController(controller);
        }
    }