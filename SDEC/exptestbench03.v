module exptestbench03;
reg [3:0] a,b;
wire [4:0] sum;
assign sum=a+b;
initial begin
repeat(10) begin
a=$urandom_range(0,9);
b=$urandom_range(0,9);
#10 $display("a=%0d b=%0d sum=%0d",a,b,sum);
end
#20 $finish;
end
endmodule