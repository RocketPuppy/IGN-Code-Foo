<?php

class Board{
    public static function display(){
        $board = file_get_contents('board.html');
        echo "<html><head>";
        echo "<link rel='stylesheet' href='board.css' type='text/css' />";
        echo "</head><body>";
        echo $board;
        echo "</body></html>";
    }
}
?>
