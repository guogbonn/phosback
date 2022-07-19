def receipt(obj):
    """
    student_name
    conf
    course_title
    course_price
    sub_total
    tax
    final_total
    terms_link
    unsubscribe_link
    """
    return f"""
    <body style="width: 100%;background-color: #ffffff;margin: 0;padding: 0;-webkit-font-smoothing: antialiased;text-align: center;  height: 100vh;">
<table width="100%" height="100%" border="0" cellspacing="0" cellpadding="10">
<tbody>
<tr>
  <td bgcolor="#222222" align="center" style="padding: 15px 0;"><div align="center" style="width: 100%;">
        <h1 style="color:white"> Phostrino
    </h1>
  </div>
    <div align="center" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:center;display:block;font-family: 'Lato', sans-serif;font-size:14px; color: #AAA; font-weight:300;">Thank You for Registering {obj["student_name"]}</div></td>
</tr>
<tr>
  <td align="center"><table width="100%" border="0" cellspacing="5" cellpadding="10" align="center" style="max-width:600px;">
      <tbody>

        <tr>
          <td align="center">
            <div align="center" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:center;display:block;font-family: 'Lato', sans-serif;font-size:14px; color: #555; font-weight:300;">Confirmation Code: <b>{obj["conf"]}</b> </div>

        </td></tr>


        <tr>
          <td align="center" valign="top"><table width="100%" border="0" cellspacing="5" cellpadding="10" align="center">
              <tbody>
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0" align="left">
                  <td style="border-collapse:collapse!important;vertical-align:middle;display:table-cell;width:auto!important;padding:12px 0 5px" align="center" valign="middle"><p style="color:#222222;text-align:center;line-height:0;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:#d9d9d9;display:block;margin:0;padding:0" align="left"></p></td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:middle;text-align:center;display:table-cell;width:120px!important;font-family: 'Lato', sans-serif;font-size:12px;font-weight:normal;text-transform:uppercase;white-space:pre-wrap;padding:12px 10px 5px" align="center" valign="middle">Order Summary</td>
                  <td style="border-collapse:collapse!important;vertical-align:middle;display:table-cell;width:auto!important;padding:12px 0 5px" align="center" valign="middle"><p style="color:#222222;text-align:center;line-height:0;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:#d9d9d9;display:block;margin:0;padding:0" align="left"></p></td>
                </tr>
              </tbody>
            </table>
            <br><table width="100%" border="0" cellspacing="5" cellpadding="0" align="center">
              <tbody>

                <!-- Repeat Per Product -->
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0;" align="left">
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top"><span style="font-weight:normal;">{obj["course_title"]}</span><br>



                </td><td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:right;display:table-cell;width:auto!important;font-family: 'Lato', sans-serif;font-size:14px;" align="right" valign="top"><span style="font-weight: normal;">${obj["course_price"]}</span>

                </td></tr>
                <tr>
                  <td height="10px">&nbsp;</td>
                </tr>
                <!-- End Repeat Per Product -->

              </tbody>
            </table>

<!-- Price Breakdown -->

            <table width="100%" border="0" cellspacing="5" cellpadding="0" align="center">
              <tbody>
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0;" align="left">
                  <td>&nbsp;</td>
                  <td colspan="2" style="border-collapse:collapse!important;vertical-align:middle;display:table-cell;width:auto!important;padding:12px 0 5px" align="center" valign="middle"><p style="color:#222222;text-align:center;line-height:0;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:#d9d9d9;display:block;margin:0;padding:0" align="left"></p></td>
                </tr>
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0;" align="left">
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;width:20px!important;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top">&nbsp;</td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top"><span style="font-weight:300;">Subtotal</span><span style="font-weight:300; margin-bottom: 20px ;"></span></td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:right;display:table-cell;width:auto!important;font-family: 'Lato', sans-serif;font-size:14px;" align="right" valign="top"><span style="font-weight: 300;">${obj["sub_total"]}</span><span style="text-decoration: line-through; font-weight:300; color: #CCC;"></span></td>
                </tr>


<!-- End CRV -->

<!-- Tax-->
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0;" align="left">
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;width:20px!important;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top">&nbsp;</td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top"><span style="font-weight:300;">Tax</span><span style="font-weight:300; margin-bottom: 20px ;"></span></td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:right;display:table-cell;width:auto!important;font-family: 'Lato', sans-serif;font-size:14px;" align="right" valign="top"><span style="font-weight: 300;">${obj["tax"]} </span></td>
                </tr>
<!-- End Tax -->
<!-- Tax-->

<!-- End Tax -->
<!-- Default Delivery Fee -->

<!-- End Default Delivery Fee -->

<!-- Delivery Fee Waived -->


<!-- End Delivery Fee Waived -->

<!-- Promo Code -->

<!-- End Promo Code -->
<!-- Tip-->

<!-- End Tip-->
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0;" align="left">
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;width:20px!important;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top">&nbsp;</td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;font-family: 'Lato', sans-serif;font-size:14px;" align="left" valign="top"><span style="font-weight:normal;">Total</span></td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:right;display:table-cell;width:auto!important;font-family: 'Lato', sans-serif;font-size:14px;" align="right" valign="top"><span style="font-weight: normal;">${obj["final_total"]}</span></td>
                </tr>

              </tbody>
            </table>

<!-- End Price Breakdown -->

            <table width="100%" border="0" cellspacing="5" cellpadding="10" align="center">
              <tbody>
                <tr style="vertical-align:top;text-align:left;width:100%;padding:0" align="left">
                  <td style="border-collapse:collapse!important;vertical-align:middle;display:table-cell;width:auto!important;padding:12px 0 5px" align="center" valign="middle"><p style="color:#222222;text-align:center;line-height:0;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:#d9d9d9;display:block;margin:0;padding:0" align="left"></p></td>
                  <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:middle;text-align:center;display:table-cell;width:120px!important;font-family: 'Lato', sans-serif;font-size:12px;font-weight:normal;text-transform:uppercase;white-space:pre-wrap;padding:12px 10px 5px;" align="center" valign="middle"></td>
                  <td style="border-collapse:collapse!important;vertical-align:middle;display:table-cell;width:auto!important;padding:12px 0 5px" align="center" valign="middle"><p style="color:#222222;text-align:center;line-height:0;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:#d9d9d9;display:block;margin:0;padding:0" align="left"></p></td>
                </tr>
              </tbody>
            </table>
            <table width="100%" border="0" cellspacing="5" cellpadding="10" align="center">
              <tbody>
                <tr>
                  <td>

                    <div align="center" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:center;display:block;font-family: 'Lato', sans-serif;font-size: 32px;color: black; font-weight:400;margin-top: 20px;"><strong>${obj["final_total"]}</strong></div>
                    <!--<div align="center" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:center;display:block;font-family: 'Lato', sans-serif;font-size:14px; color: #1BA9BA; font-weight:300; font-style:italic">*Includes Tax</div></td> -->
                </td></tr>
              </tbody>
            </table></td>
        </tr>
      </tbody>
    </table></td>
</tr>

<tr>
  <td bgcolor="#222222"><div align="center" style="margin-top: 10px; color:white;  font-size: 12px; margin-bottom: 5px;">
    <a style="color:#CCC; text-decoration:none; font-family: 'Lato', sans-serif;" href="mailto:support@phostrino.com" target="_blank">support@phostrino.com</a>
    <a style="color:#CCC; text-decoration:none; font-family: 'Lato', sans-serif; border-right:1px solid #CCC; border-left:1px solid #CCC; padding:0 5px; margin: 0 5px;" href=" {obj["terms_link"]}" target="_blank">Terms of Service </a>
    <a style="color:#CCC; text-decoration:none; font-family: 'Lato', sans-serif;" href=" {obj["unsubscribe_link"]} " target="_blank">Unsubscribe</a></div>
    <div align="center" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:center;display:block;font-family: 'Lato', sans-serif;font-size:10px; color: #AAA; font-weight:300; margin-bottom: 10px;">23133 Woodward Ave #201 Ferndale, Mi 48220</div></td>
</tr>
</tbody>
</table>



</body>

    """


def course_welcome(obj):
    return f"""
  <body style="width: 100%;background-color: #ffffff;margin: 0;padding: 0;-webkit-font-smoothing: antialiased;text-align: center;overflow-x: hidden;height: auto;">
   <table width="100%" height="100%" border="0" cellspacing="0" cellpadding="10">
   <tbody>
   <tr>
     <td bgcolor="#222222" align="center" style="padding: 15px 0;height: 10px;"><div align="center" style="width: 100%;">
           <h1 style="color:white" > Phostrino
       </h1>
     </div>
       </td>
   </tr>
   <tr>
     <td align="" style="
       position: relative;
       justify-content: center;
       display: flex;
   "><table width="100%" border="0" cellspacing="5" cellpadding="10" align="center" style="position: absolute;max-width:600px;top: 0%;">
         <tbody>

           <tr>
             <td align="center">


           </td></tr>


           <tr>
             <td align="center" valign="top"><table width="100%" border="0" cellspacing="5" cellpadding="10" align="center">
                 <tbody>
                   <tr style="vertical-align:top;text-align:left;width:100%;padding:0" align="left">



                   </tr>
                 </tbody>
               </table>
               <br><table width="100%" border="0" cellspacing="5" cellpadding="0" align="center" style="
       margin-bottom: 0px;
       margin-top: -100;
       margin-top: -50px;
   ">
                 <tbody>

                   <!-- Repeat Per Product -->
                   <tr style="vertical-align:top;text-align:left;width:100%;padding:0;" align="left">
                     <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:left;display:table-cell;font-family: 'Lato', sans-serif;font-size:14px;"><br>
       Welcome { obj["student_name"]},

       <br><br><br>

       Thank you for signing up for the <b> {obj["course_title"]} Course </b>. We are excited to have you as a student!
       <br><br><br>
       Course Dates: <b> {space_dates(obj["course_dates"])} </b>
       <br> <br>
       <span>Session Time: <b> {obj["course_time"]}  </b> </span>
       <br> <br>
       Course Days: <b>{obj["course_days"]}  </b>
        <br> <br>
        Course Length: <b>10 Sessions </b>
       <br><br>
       Course Zoom Link: <a href=" {obj["zoom_link"]} ">{obj["course_title"]} Zoom Link</a> <br><br><br> You might find it easier to download Zoom before hand: <br><br><br>

   <a href="https://zoom.us/download">Zoom download </a> <br><br><br>  In the meantime, here are some resources our instructors have found useful, you can look through them at your pleasure. This is <b>not</b> required knowledge. <br>
       <br>
   <a href="https://docs.python.org/3/tutorial/index.html">Python Documentation</a> <br> <br>

       <a href="https://www.pythoncheatsheet.org/">Python Cheat Sheet</a>

      <br>
       <br>
       <br>

   Thank you. <br>
   Regards, <br>
   Phostrino Team <br> <br> <br>




                   </td></tr>
                   <tr>
                     <td height="10px">&nbsp;</td>
                   </tr>
                   <!-- End Repeat Per Product -->

                 </tbody>
               </table>


               <table width="100%" border="0" cellspacing="5" cellpadding="10" align="center">
                 <tbody>

                 </tbody>
               </table>
               <table width="100%" border="0" cellspacing="5" cellpadding="10" align="center">
                 <tbody>
                   <tr>
                     <td>


                   </td></tr>
                 </tbody>
               </table></td>
           </tr>
         </tbody>
       </table></td>
   </tr>

   <tr style="position: absolute;bottom: -90px;background-color: #222222;width: 100%;align-items: center;">
     <td bgcolor="#222222" style="
       height: 10px;
   "><div align="center" style="margin-top: 10px; color:white;  font-size: 12px; margin-bottom: 5px;">
       <a style="color:#CCC; text-decoration:none; font-family: 'Lato', sans-serif;" href="mailto:support@phostrino.com" target="_blank">support@phostrino.com</a>
       <a style="color:#CCC; text-decoration:none; font-family: 'Lato', sans-serif; border-right:1px solid #CCC; border-left:1px solid #CCC; padding:0 5px; margin: 0 5px;" href=" {obj["terms_link"]}" target="_blank">Terms of Service </a>
       <a style="color:#CCC; text-decoration:none; font-family: 'Lato', sans-serif;" href=" {obj["unsubscribe_link"]} " target="_blank">Unsubscribe</a></div>
       <div align="center" style="word-break:break-word;border-collapse:collapse!important;vertical-align:top;text-align:center;display:block;font-family: 'Lato', sans-serif;font-size:10px; color: #AAA; font-weight:300; margin-bottom: 10px;">23133 Woodward Ave #201 Ferndale, Mi 48220</div></td>
   </tr>
   </tbody>
   </table>

   </body>
    """

def space_dates(date):
    date = date.split('-')
    return " - ".join(date)
