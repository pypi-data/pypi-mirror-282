module Gain #(
    parameter DW = 24,
    parameter COEFW = 18,
    parameter COEFQ = 16
) (
    input  logic clk,
    input  logic rst,

    input  logic signed [DW-1:0] s_axis_tdata,
    input  logic s_axis_tvalid,
    output logic s_axis_tready,

    output logic signed [DW-1:0] m_axis_tdata,
    output logic m_axis_tvalid,
    input  logic m_axis_tready,

    input  logic signed [COEFW-1:0] k
);

logic signed [DW-1:0] skid_tdata;
logic skid_tvalid, skid_tready;

Skid #(
    .DW(DW)
) skid_i (
    .clk(clk),
    .rst(rst),
    .s_axis_tdata(s_axis_tdata),
    .s_axis_tvalid(s_axis_tvalid),
    .s_axis_tready(s_axis_tready),
    .m_axis_tdata(skid_tdata),
    .m_axis_tvalid(skid_tvalid),
    .m_axis_tready(skid_tready)
);

logic signed [COEFW-1:0] k_reg;
/* verilator lint_off UNUSED */
logic signed [DW+COEFW-1:0] mult;
/* verilator lint_on UNUSED */

// logic mult_valid = 0;
// always @(posedge clk) begin
//     mult <= k * s_axis_tdata;
// end
assign mult = k_reg * skid_tdata;

assign skid_tready = (!m_axis_tvalid || m_axis_tready);

always @(posedge clk) begin
    k_reg <= k;

    if (m_axis_tvalid && m_axis_tready) begin
        m_axis_tvalid <= 0;
    end

    if (skid_tvalid && skid_tready) begin
        m_axis_tdata <= mult[COEFQ+DW-1:COEFQ];
        m_axis_tvalid <= 1;
    end

    if (rst) begin
        m_axis_tvalid <= 0;
    end    
end



endmodule
