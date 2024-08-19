# GrepVulnRD
Listado para Buscar Vulnerabilidad en Código

##1. Cross-Site Scripting (XSS)
PHP

Codigo

grep -Ri "echo" .
grep -Ri "print" .
grep -Ri "htmlspecialchars(" .
grep -Ri "htmlentities(" .
grep -Ri "strip_tags(" .
grep -Ri "addslashes(" .
grep -Ri "\$_GET" . | grep "echo"
grep -Ri "\$_POST" . | grep "echo"
grep -Ri "\$_REQUEST" . | grep "echo"
grep -Ri "\$_COOKIE" . | grep "echo"

JavaScript

Codigo

grep -Ri "document.write(" .
grep -Ri "innerHTML" .
grep -Ri "outerHTML" .
grep -Ri "eval(" .
grep -Ri "setTimeout(" .
grep -Ri "setInterval(" .
grep -Ri "location=" .
grep -Ri "onerror=" .

Ruby

Codigo

grep -Ri "render" .
grep -Ri "html_safe" .
grep -Ri "content_tag" .
grep -Ri "raw(" .
grep -Ri "escape_html(" .

##2. Command Execution
PHP

Codigo

grep -Ri "shell_exec(" .
grep -Ri "system(" .
grep -Ri "exec(" .
grep -Ri "popen(" .
grep -Ri "passthru(" .
grep -Ri "proc_open(" .
grep -Ri "pcntl_exec(" .
grep -Ri "shell_exec(" .
grep -Ri "proc_open(" .

Python

Codigo

grep -Ri "subprocess.call(" .
grep -Ri "subprocess.Popen(" .
grep -Ri "os.system(" .
grep -Ri "os.popen(" .
grep -Ri "exec(" .
grep -Ri "eval(" .
grep -Ri "execfile(" .

Ruby

Codigo

grep -Ri "system(" .
grep -Ri "exec(" .
grep -Ri "IO.popen(" .
grep -Ri "Kernel.`(" .
grep -Ri "Kernel.system(" .

##3. Code Execution
PHP

Codigo

grep -Ri "eval(" .
grep -Ri "assert(" .
grep -Ri "preg_replace" . | grep "/e"
grep -Ri "create_function(" .
grep -Ri "call_user_func(" .
grep -Ri "call_user_func_array(" .

Python

Codigo

grep -Ri "eval(" .
grep -Ri "exec(" .
grep -Ri "execfile(" .
grep -Ri "compile(" .
grep -Ri "getattr(" .
grep -Ri "setattr(" .

Ruby

Codigo

grep -Ri "eval(" .
grep -Ri "Kernel.eval(" .
grep -Ri "instance_eval(" .
grep -Ri "class_eval(" .
grep -Ri "define_method(" .

##4. SQL Injection
PHP

Codigo

grep -Ri "\$sql" .
grep -Ri "\$sql" . | grep "\$_"
grep -Ri "mysql_query(" .
grep -Ri "mysqli_query(" .
grep -Ri "PDO->query(" .
grep -Ri "PDO->exec(" .
grep -Ri "mysqli_prepare(" .
grep -Ri "PDO->prepare(" .

Python

Codigo

grep -Ri "execute(" . | grep "cursor"
grep -Ri "fetchall(" .
grep -Ri "fetchone(" .
grep -Ri "db.execute(" .
grep -Ri "db.cursor(" .
grep -Ri "params=(" .

JavaScript (Node.js)

Codigo

grep -Ri "query(" . | grep "db"
grep -Ri "execute(" . | grep "db"
grep -Ri "preparedStatement(" .
grep -Ri "sql.format(" .

##5. Information Leak
PHP

Codigo

grep -Ri "phpinfo" .
grep -Ri "info.php" .
grep -Ri "show_source(" .
grep -Ri "var_dump(" .
grep -Ri "print_r(" .
grep -Ri "debug_backtrace(" .

Python

Codigo

grep -Ri "sys.version" .
grep -Ri "platform.platform" .
grep -Ri "print(" .
grep -Ri "logging.debug(" .

##6. Find Dev and Debug Modes
PHP

Codigo

grep -Ri "debug" .
grep -Ri "\$_GET['debug']" .
grep -Ri "\$_GET['test']" .
grep -Ri "error_reporting(" .
grep -Ri "display_errors" .

Python

Codigo

grep -Ri "DEBUG" .
grep -Ri "settings.DEBUG" .
grep -Ri "test" .
grep -Ri "logging.debug(" .

##7. RFI/LFI (Remote File Inclusion/Local File Inclusion)
PHP

Codigo

grep -Ri "file_include" .
grep -Ri "include(" .
grep -Ri "require(" .
grep -Ri "require(\$file)" .
grep -Ri "include_once(" .
grep -Ri "require_once(" .
grep -Ri "include(" . | grep "\$_"
grep -Ri "require(" . | grep "\$_"

Python

Codigo

grep -Ri "open(" .
grep -Ri "import(" .
grep -Ri "file(" .
grep -Ri "os.path.join(" .
grep -Ri "pathlib.Path(" .

Ruby

Codigo

grep -Ri "require(" .
grep -Ri "load(" .
grep -Ri "require_relative(" .

##8. Miscellaneous
PHP

Codigo

grep -Ri "header(" . | grep "\$_"
grep -Ri '$_SERVER["HTTP_USER_AGENT"]' .
grep -Ri "preg_replace" . | grep "/e"
grep -Ri "mail(" .
grep -Ri "socket_create(" .

Python

Codigo

grep -Ri "request.headers.get(" .
grep -Ri "request.META.get(" .
grep -Ri "send_mail(" .
grep -Ri "socket.socket(" .

##9. Path Traversal
PHP

Codigo

grep -Ri "file_get_contents(" .
grep -Ri "fopen(" .
grep -Ri "readfile(" .
grep -Ri "file(" .
grep -Ri "realpath(" .
grep -Ri "include(" . | grep "\.\."
grep -Ri "require(" . | grep "\.\."

Python

Codigo

grep -Ri "open(" .
grep -Ri "os.path.join(" .
grep -Ri "pathlib.Path(" .
grep -Ri "file(" .
grep -Ri "os.chdir(" .
grep -Ri "os.path.abspath(" .

JavaScript (Node.js)

Codigo

grep -Ri "fs.readFile(" .
grep -Ri "path.join(" .
grep -Ri "path.resolve(" .
grep -Ri "fs.createReadStream(" .
grep -Ri "fs.createWriteStream(" .

##10. Insecure Direct Object References (IDOR)
PHP

Codigo

grep -Ri "\$_GET" . | grep "file_get_contents(" .
grep -Ri "\$_POST" . | grep "fopen(" .
grep -Ri "\$_REQUEST" . | grep "include(" .

Python

Codigo

grep -Ri "\$_GET" . | grep "open(" .
grep -Ri "\$_POST" . | grep "file(" .
grep -Ri "\$_REQUEST" . | grep "pathlib.Path(" .

##11. Improper Error Handling
PHP

Codigo

grep -Ri "error_log(" .
grep -Ri "trigger_error(" .
grep -Ri "set_error_handler(" .
grep -Ri "try {" .
grep -Ri "catch (" .

Python

Codigo

grep -Ri "logging.error(" .
grep -Ri "logging.exception(" .
grep -Ri "try:" .
grep -Ri "except:" .

##12. Hardcoded Credentials
PHP

Codigo

grep -Ri "password" .
grep -Ri "db_password" .
grep -Ri "username" .
grep -Ri "api_key" .

Python

Codigo

grep -Ri "password" .
grep -Ri "db_password" .
grep -Ri "username" .
grep -Ri "api_key" .
grep -Ri "secret_key" .

##13. Unsafe File Uploads
PHP

Codigo

grep -Ri "move_uploaded_file(" .
grep -Ri "tmp_name" .
grep -Ri "file_uploads" .

Python

Codigo

grep -Ri "save" .
grep -Ri "upload" .
grep -Ri "tempfile" .
