def handle_windows_terminal():
    """
    Handle specific settings for Windows CMD and PowerShell.
    """
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Get the handle to the standard output device (console)
        handle = kernel32.GetStdHandle(-11)
        # Set the console mode to enable virtual terminal processing
        # Virtual terminal processing allows the console to interpret ANSI escape sequences
        # which are used for text formatting, such as changing text color, bold, underline, etc.
        kernel32.SetConsoleMode(handle, 7)
    except Exception as e:
        print(f"Error handling Windows terminal: {e}")