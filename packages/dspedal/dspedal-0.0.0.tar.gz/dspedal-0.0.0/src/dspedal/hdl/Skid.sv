module Skid #(
    parameter DW = 24
) (
    input  logic clk,
    input  logic rst,

    input  logic [DW-1:0] s_axis_tdata,
    input  logic s_axis_tvalid,
    output logic s_axis_tready,

    output logic [DW-1:0] m_axis_tdata,
    output logic m_axis_tvalid,
    input  logic m_axis_tready
);

logic [DW-1:0] skid_tdata = 0;
logic skid_tvalid = 0;

assign s_axis_tready = !skid_tvalid;

always @(posedge clk) begin
    // Output data was accepted
    if (m_axis_tvalid && m_axis_tready) begin
        m_axis_tvalid <= 0;
    end

    if ((s_axis_tvalid && s_axis_tready) && (m_axis_tvalid && !m_axis_tready)) begin
        // Incoming data is valid but the output is stalled. Load into skid buffer.
        skid_tvalid <= 1;
    end else if (m_axis_tready) begin
        // The buffer will always be emptied if the downstream module is ready.
        skid_tvalid <= 0;
    end

    // There is data available and the output can accept data this clock cycle.
    if ((s_axis_tvalid || skid_tvalid) && (!m_axis_tvalid || m_axis_tready)) begin
        // Read from the skid first, otherwise use s_axis_tdata
        m_axis_tdata <= skid_tvalid ? skid_tdata : s_axis_tdata;
        m_axis_tvalid <= 1;
    end

    // An input transaction was buffered into the skid.
    if (s_axis_tvalid && s_axis_tready) begin
        skid_tdata <= s_axis_tdata;
    end

    if (rst) begin
        m_axis_tvalid <= 0;
        skid_tvalid <= 0;
    end
end
    
endmodule
