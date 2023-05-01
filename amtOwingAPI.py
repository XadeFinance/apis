from subprocess import check_output
from flask import Flask, request
from json import loads
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
import time

load_dotenv()

emailPass = getenv("emailPass")
v2Key = getenv("v2Key")
connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)
db = client["remmitex"]
collection2 = db["mainnet"]
collection = db["testnet"]

app = Flask(__name__)

@app.route("/testnet", methods=["POST"])
def testnetPart1():
    html = """\
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
  <head>
    <title> Welcome to Coded Mails </title>
    <!--[if !mso]>
		<!-- -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!--
		<![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
      #outlook a {
        padding: 0;
      }

      body {
        margin: 0;
        padding: 0;
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }

      table,
      td {
        border-collapse: collapse;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
      }

      img {
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
        -ms-interpolation-mode: bicubic;
      }

      p {
        display: block;
        margin: 13px 0;
      }
    </style>
    <!--[if mso]>
		<xml>
			<o:OfficeDocumentSettings>
				<o:AllowPNG/>
				<o:PixelsPerInch>96</o:PixelsPerInch>
			</o:OfficeDocumentSettings>
		</xml>
		<![endif]-->
    <!--[if lte mso 11]>
		<style type="text/css">
          .mj-outlook-group-fix { width:100% !important; }
        </style>
		<![endif]-->
    <!--[if !mso]>
		<!-->
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet" type="text/css" />
    <style type="text/css">
      @import url(https://fonts.googleapis.com/css?family=Lato:300,400,700);
    </style>
    <!--
		<![endif]-->
    <style type="text/css">
      @media only screen and (min-width:480px) {
        .mj-column-per-100 {
          width: 100% !important;
          max-width: 100%;
        }
      }
    </style>
    <style type="text/css">
      @media only screen and (max-width:480px) {
        table.mj-full-width-mobile {
          width: 100% !important;
        }

        td.mj-full-width-mobile {
          width: auto !important;
        }
      }
    </style>
    <style type="text/css">
      a,
      span,
      td,
      th {
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
      }
    </style>
  </head>
  <body style="background-color:#ffffff;" data-new-gr-c-s-check-loaded="14.1104.0" data-gr-ext-installed="">
    <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Tera Baap(0xfb2...Ot5) has sent you $0.69 on Polygon Mainnet through Xade </div>
    <div style="background-color:#ffffff;">
      <!--[if mso | IE]>
			<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
				<tr>
					<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
						<![endif]-->
      <div style="margin:0px auto;max-width:600px;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
                <!--[if mso | IE]>
											<table role="presentation" border="0" cellpadding="0" cellspacing="0">
												<tr>
													<td
               class="" style="vertical-align:top;width:600px;"
            >
														<![endif]-->
                <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                    <tbody>
                      <tr>
                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:150px;"></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <!--[if mso | IE]>
																			<table role="presentation" border="0" cellpadding="0" cellspacing="0">
																				<tr>
																					<td height="20" style="vertical-align:top;height:20px;">
																						<![endif]-->
                          <div style="height:20px;"></div>
                          <!--[if mso | IE]>
																					</td>
																				</tr>
																			</table>
																			<![endif]-->
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:600px;">
                                  <a href="https://google.com" target="_blank" style="color: #2e58ff; text-decoration: none;">
                                    <img alt="image description" height="auto" src="https://mint.xade.finance/logo.png" style="border:0;display:block;outline:none;text-decoration:none;height:50%;width:100%;font-size:13px;" width="600" />
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <!--[if mso | IE]>
													</td>
												</tr>
											</table>
											<![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!--[if mso | IE]>
					</td>
				</tr>
			</table>
			<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
				<tr>
					<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
						<![endif]-->
      <div style="margin:0px auto;max-width:600px;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                <!--[if mso | IE]>
											<table role="presentation" border="0" cellpadding="0" cellspacing="0">
												<tr>
													<td
               class="" style="vertical-align:top;width:600px;"
            >
														<![endif]-->
                <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                    <tbody>
                      <tr>
                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <div style="font-family:Lato,'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Woohoo! You've just received a payment of $0.69 from Tera Baap, who clearly understands the value of your awesomeness. Time to celebrate with a victory dance and maybe a little online shopping spree (responsibly, of course). Thanks, Tera Baap, you're the real MVP!
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <div style="font-family:Lato,'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Download Xade Mobile App to claim your payment </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                            <tbody>
                              <tr>
                                <td align="center" role="presentation" style="border:none;border-radius:3px;cursor:auto;mso-padding-alt:10px 25px;" valign="middle">
                                  <br />
                                  <br />
                                  <br />
                                  <a href="https://google.com" style="display: inline-block; background: #0080FF; color: white; font-family: Lato,'Helvetica Neue',Helvetica,Arial,sans-serif; font-size: 18px; font-weight: bold; line-height: 40px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; width:auto; border-radius:16px;" target="_blank"> Claim Now </a>
                                  <div style="font-family:Lato,'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                                    <p style="text-align:left;font-weight:bold;">Please make sure the email is from the official Xade email: <a href="mailto:support@xade.finance">support@xade.finance</a>
                                    </p>
                                    <br /> Best, <br /> Team Xade.
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <!--[if mso | IE]>
															</td>
														</tr>
													</table>
													<![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!--[if mso | IE]>
							</td>
						</tr>
					</table>
					<![endif]-->
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fafafa;background-color:#fafafa;width:100%;">
        <tbody>
          <tr>
            <td>
              <!--[if mso | IE]>
									<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
										<tr>
											<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
												<![endif]-->
              <div style="margin:0px auto;max-width:600px;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                  <tbody>
                    <tr>
                      <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                        <!--[if mso | IE]>
																	<table role="presentation" border="0" cellpadding="0" cellspacing="0">
																		<tr>
																			<td
                 class="" width="600px"
              >
																				<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
																					<tr>
																						<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
																							<![endif]-->
                        <div style="margin:0px auto;max-width:600px;">
                          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                            <tbody>
                              <tr>
                                <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                                  <!--[if mso | IE]>
																												<table role="presentation" border="0" cellpadding="0" cellspacing="0">
																													<tr>
																														<td
               class="" style="vertical-align:top;width:600px;"
            >
																															<![endif]-->
                                  <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                            <!--[if mso | IE]>
																																				<table
         align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
																																					<tr>
																																						<td>
																																							<![endif]-->
                                            <![endif]-->
																																						</td>
																																					</tr>
																																				</tbody>
																																			</table>
																																		</div>
																																		<!--[if mso | IE]>
                                          </td>
                                        </tr>
                                    </table>
                                    <![endif]-->
																														</td>
																													</tr>
																												</tbody>
																											</table>
																										</div>
																										<!--[if mso | IE]>
                                </td>
                              </tr>
                          </table>
                      </td>
                    </tr>
                </table>
                <![endif]-->
																			</td>
																		</tr>
																	</tbody>
																</table>
															</div>
															<!--[if mso | IE]>
            </td>
          </tr>
      </table>
      <![endif]-->
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</body>
"""
    data = request.get_json()["data"]
    command = ["node", "decrypt.js", v2Key, data]
    decrypted_data = check_output(command)
	

    obj = loads(decrypted_data)
    senderName = obj.get("senderName")
    receiver = obj.get("receiver")
    amount = float(obj.get("amount"))
    timestamp = int(obj.get("timestamp"))
    senderAddr = obj.get("senderAddr")
    senderAddr = senderAddr[:5] + "..." + senderAddr[-3:]
    doc = collection.find_one({"Email": receiver})
    print(doc)
    if doc:
        current_timestamp = doc.get("timestamp")
        diff = abs(current_timestamp - timestamp)
        max_diff = 60 * 1000  # minimum difference of 1 minute in 
        if diff <= max_diff:
		        print("Timestamp is okay")
        else:
		        return "madarchod", 403
    msg = MIMEMultipart()
    msg[
        "Subject"
    ] = f"{senderName}({senderAddr}) has sent you ${amount} on Polygon Testnet through Xade"
    msg["From"] = "Xade Finance<support@xade.finance>"
    msg["To"] = receiver
    msg.attach(MIMEText(html, "html"))

    mailserver = SMTP_SSL("smtpout.secureserver.net", 465)
    mailserver.ehlo()
    mailserver.login("support@xade.finance", emailPass)

    mailserver.sendmail("support@xade.finance", receiver, msg.as_string())

    mailserver.quit()
    current_timestamp = int(time.time() * 1000)  # current timestamp in milliseconds
    if doc:
	    collection.update_one(
		      {"Email": receiver},
		      {"$set": {"Amount": doc.get("Amount") + amount, "timestamp": datetime.datetime.now()}}
	    )

    else:
	    collection.insert_one(
		      {"Email": receiver, "Amount": amount, "timestamp": datetime.datetime.now()}
	    )


    return "donezo", 200

@app.route("/mainnet", methods=["POST"])
def mainnetPart1():
    html = """\
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
  <head>
    <title> Welcome to Coded Mails </title>
    <!--[if !mso]>
		<!-- -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!--
		<![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
      #outlook a {
        padding: 0;
      }

      body {
        margin: 0;
        padding: 0;
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }

      table,
      td {
        border-collapse: collapse;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
      }

      img {
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
        -ms-interpolation-mode: bicubic;
      }

      p {
        display: block;
        margin: 13px 0;
      }
    </style>
    <!--[if mso]>
		<xml>
			<o:OfficeDocumentSettings>
				<o:AllowPNG/>
				<o:PixelsPerInch>96</o:PixelsPerInch>
			</o:OfficeDocumentSettings>
		</xml>
		<![endif]-->
    <!--[if lte mso 11]>
		<style type="text/css">
          .mj-outlook-group-fix { width:100% !important; }
        </style>
		<![endif]-->
    <!--[if !mso]>
		<!-->
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet" type="text/css" />
    <style type="text/css">
      @import url(https://fonts.googleapis.com/css?family=Lato:300,400,700);
    </style>
    <!--
		<![endif]-->
    <style type="text/css">
      @media only screen and (min-width:480px) {
        .mj-column-per-100 {
          width: 100% !important;
          max-width: 100%;
        }
      }
    </style>
    <style type="text/css">
      @media only screen and (max-width:480px) {
        table.mj-full-width-mobile {
          width: 100% !important;
        }

        td.mj-full-width-mobile {
          width: auto !important;
        }
      }
    </style>
    <style type="text/css">
      a,
      span,
      td,
      th {
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
      }
    </style>
  </head>
  <body style="background-color:#ffffff;" data-new-gr-c-s-check-loaded="14.1104.0" data-gr-ext-installed="">
    <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> Tera Baap(0xfb2...Ot5) has sent you $0.69 on Polygon Mainnet through Xade </div>
    <div style="background-color:#ffffff;">
      <!--[if mso | IE]>
			<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
				<tr>
					<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
						<![endif]-->
      <div style="margin:0px auto;max-width:600px;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
                <!--[if mso | IE]>
											<table role="presentation" border="0" cellpadding="0" cellspacing="0">
												<tr>
													<td
               class="" style="vertical-align:top;width:600px;"
            >
														<![endif]-->
                <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                    <tbody>
                      <tr>
                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:150px;"></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size:0px;word-break:break-word;">
                          <!--[if mso | IE]>
																			<table role="presentation" border="0" cellpadding="0" cellspacing="0">
																				<tr>
																					<td height="20" style="vertical-align:top;height:20px;">
																						<![endif]-->
                          <div style="height:20px;"></div>
                          <!--[if mso | IE]>
																					</td>
																				</tr>
																			</table>
																			<![endif]-->
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                            <tbody>
                              <tr>
                                <td style="width:600px;">
                                  <a href="https://google.com" target="_blank" style="color: #2e58ff; text-decoration: none;">
                                    <img alt="image description" height="auto" src="https://mint.xade.finance/logo.png" style="border:0;display:block;outline:none;text-decoration:none;height:50%;width:100%;font-size:13px;" width="600" />
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <!--[if mso | IE]>
													</td>
												</tr>
											</table>
											<![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!--[if mso | IE]>
					</td>
				</tr>
			</table>
			<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
				<tr>
					<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
						<![endif]-->
      <div style="margin:0px auto;max-width:600px;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                <!--[if mso | IE]>
											<table role="presentation" border="0" cellpadding="0" cellspacing="0">
												<tr>
													<td
               class="" style="vertical-align:top;width:600px;"
            >
														<![endif]-->
                <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                    <tbody>
                      <tr>
                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <div style="font-family:Lato,'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Woohoo! You've just received a payment of $0.69 from Tera Baap, who clearly understands the value of your awesomeness. Time to celebrate with a victory dance and maybe a little online shopping spree (responsibly, of course). Thanks, Tera Baap, you're the real MVP!
                      </tr>
                      <tr>
                        <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <div style="font-family:Lato,'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">Download Xade Mobile App to claim your payment </div>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                            <tbody>
                              <tr>
                                <td align="center" role="presentation" style="border:none;border-radius:3px;cursor:auto;mso-padding-alt:10px 25px;" valign="middle">
                                  <br />
                                  <br />
                                  <br />
                                  <a href="https://google.com" style="display: inline-block; background: #0080FF; color: white; font-family: Lato,'Helvetica Neue',Helvetica,Arial,sans-serif; font-size: 18px; font-weight: bold; line-height: 40px; margin: 0; text-decoration: none; text-transform: uppercase; padding: 10px 25px; mso-padding-alt: 0px; width:auto; border-radius:16px;" target="_blank"> Claim Now </a>
                                  <div style="font-family:Lato,'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#434245;">
                                    <p style="text-align:left;font-weight:bold;">Please make sure the email is from the official Xade email: <a href="mailto:support@xade.finance">support@xade.finance</a>
                                    </p>
                                    <br /> Best, <br /> Team Xade.
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <!--[if mso | IE]>
															</td>
														</tr>
													</table>
													<![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!--[if mso | IE]>
							</td>
						</tr>
					</table>
					<![endif]-->
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fafafa;background-color:#fafafa;width:100%;">
        <tbody>
          <tr>
            <td>
              <!--[if mso | IE]>
									<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
										<tr>
											<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
												<![endif]-->
              <div style="margin:0px auto;max-width:600px;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                  <tbody>
                    <tr>
                      <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                        <!--[if mso | IE]>
																	<table role="presentation" border="0" cellpadding="0" cellspacing="0">
																		<tr>
																			<td
                 class="" width="600px"
              >
																				<table
         align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600"
      >
																					<tr>
																						<td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
																							<![endif]-->
                        <div style="margin:0px auto;max-width:600px;">
                          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                            <tbody>
                              <tr>
                                <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                                  <!--[if mso | IE]>
																												<table role="presentation" border="0" cellpadding="0" cellspacing="0">
																													<tr>
																														<td
               class="" style="vertical-align:top;width:600px;"
            >
																															<![endif]-->
                                  <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                      <tbody>
                                        <tr>
                                          <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                            <!--[if mso | IE]>
																																				<table
         align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
      >
																																					<tr>
																																						<td>
																																							<![endif]-->
                                            <![endif]-->
																																						</td>
																																					</tr>
																																				</tbody>
																																			</table>
																																		</div>
																																		<!--[if mso | IE]>
                                          </td>
                                        </tr>
                                    </table>
                                    <![endif]-->
																														</td>
																													</tr>
																												</tbody>
																											</table>
																										</div>
																										<!--[if mso | IE]>
                                </td>
                              </tr>
                          </table>
                      </td>
                    </tr>
                </table>
                <![endif]-->
																			</td>
																		</tr>
																	</tbody>
																</table>
															</div>
															<!--[if mso | IE]>
            </td>
          </tr>
      </table>
      <![endif]-->
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</body>
"""
    data = request.get_json()["data"]
    command = ["node", "decrypt.js", v2Key, data]
    decrypted_data = check_output(command)

    obj = loads(decrypted_data)
    senderName = obj.get("senderName")
    receiver = obj.get("receiver")
    amount = obj.get("amount")
    timestamp = int(obj.get("timestamp"))
    senderAddr = obj.get("senderAddr")
    senderAddr = senderAddr[:5] + "..." + senderAddr[-3:]

    dt = datetime.fromtimestamp(timestamp, timezone.utc)
    current_dt = datetime.now(timezone.utc)
    if dt.date() == current_dt.date() and abs((dt - current_dt).total_seconds()) <= 60:
        print("Timestamp is on today's date and within a minute of the current time")
    else:
        return "madarchod", 403

    msg = MIMEMultipart()
    msg[
        "Subject"
    ] = f"{senderName}({senderAddr}) has sent you ${amount} on Polygon Testnet through Xade"
    msg["From"] = "Xade Finance<support@xade.finance>"
    msg["To"] = receiver
    msg.attach(MIMEText(html, "html"))

    mailserver = SMTP_SSL("smtpout.secureserver.net", 465)
    mailserver.ehlo()
    mailserver.login("support@xade.finance", emailPass)

    mailserver.sendmail("support@xade.finance", receiver, msg.as_string())

    mailserver.quit()

    document = {"Email": receiver, "Amount": amount}
    result = collection2.insert_one(document)

    return "donezo", 200

if __name__ == "__main__":
    app.run('127.0.0.1',8010)
