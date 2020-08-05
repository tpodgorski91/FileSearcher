# file_searcher

The project goal is to open specific file in dedicated application 
(e.g. for Windows ".txt" files it would be "Notepad") in different OS like: Windows, macOS, Linux,
based on user inputs like:

drive name where file is stored

file name (may be only portion of name)

1. DONE User chooses drive where would like to look for .txt, .jpg file.
    input()?
2. User provides either whole or part of name provided.
    DONE regex
3. User chooses specific file from the list of files that match the name (pattern).
    index
4. Program opens file.
    dictionary
