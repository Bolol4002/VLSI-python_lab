module Exp09;
mailbox m=new();
initial fork
producer();
consumer();
join

task producer;
int d=10;
m.put(d);
$display("Producer sent %0d",d);
endtask

task consumer;
int d;
m.get(d);
$display("Consumer received %0d",d);
endtask
endmodule