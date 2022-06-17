import socket
import select

ready_to_read, ready_to_write, in_error = select.select(read_list, write_list, error_list)
