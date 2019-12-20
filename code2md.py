import os

################################################################################
def code2md_gen(p_code_folder, p_md_folder, p_language, p_retain_yaml, p_code_file):

    # Check Folders
    if p_code_folder == '':
        list_all_py_files = os.listdir(p_code_folder)
    else:
        list_all_py_files = [p_code_file]

    for code_file in list_all_py_files:
    ###################################
        l_final_md = ''
        l_ti_code_format_flg = 0
        l_md_s_comment = ['-- >','// >','## >','-- > ','// > ','## > ','# MARKDOWN ', '# MARKDOWN']
        l_md_m_comment1 = 'MARKDOWN """'
        l_md_m_comment2 = '""" MARKDOWN'
        l_initial_code_open = 1
        l_ignore_flag = 0
        
        ObjFile = open(p_code_folder + code_file,"r")
        while True:
            curr_line = ObjFile.readline()
            if not curr_line:
                break

            # Handle format Single MD Comment Style
            for i in l_md_s_comment:
                curr_line = curr_line.replace(i,'')

            curr_line = curr_line.rstrip('\n').rstrip('\r')

            ##################################################
            # YAML Detection, ignore YAML if p_retain_yaml = 1
            ##################################################
            if p_retain_yaml == 1:
                if curr_line.strip() == "---" and l_ignore_flag == 0:
                    l_ignore_flag = 1
                    curr_line = ''
                    
                if l_ignore_flag == 1 and curr_line.strip() != "---":
                    curr_line = ''
                elif l_ignore_flag == 1 and curr_line.strip() == "---":
                    curr_line = ''
                    l_ignore_flag = 0


            ##########################################################
            # Every MD Block ``` detection
            ##########################################################
            if curr_line.strip() == "```" and l_initial_code_open == 1:
                curr_line = curr_line.strip() + p_language
                l_initial_code_open = 0
                l_ti_code_format_flg = 1
            elif curr_line.strip() == "```" and l_initial_code_open == 0:
                l_initial_code_open = 1 


            ###########################################
            # Handle format Multi line MD Comment Style
            ###########################################
            if curr_line.strip() == l_md_m_comment1 or curr_line.strip() == l_md_m_comment2:
                pass
                l_ti_code_format_flg = 1
            else:
                l_final_md = l_final_md + '\n' + curr_line

        ObjFile.close()

        ###############################
        # Clean the strings: l_final_md
        ###############################
        print(l_final_md.strip('\n'))

        ##############################################################
        # Write to File only if the code file is in the TI Code format
        ##############################################################
        if l_ti_code_format_flg == 1:
            f = open(md_file_folder + os.path.basename(code_file), "w")
            f.write(l_final_md)
            f.close()
        else:
            print(p_code_folder + code_file,'is not a TI MD code format file, skipping MD creation')

        # Reset flags
        l_ti_code_format_flg = 0
################################################################################



################################################################################
# DATA SETUP
################################################################################
l_language = "python"
l_retain_yaml = 1


# Test Set 1
code_file_folder = "C:\\Personal\\tinitiate\\source\\python\\python-core-language\\code\\"
md_file_folder = "C:\\Personal\\tinitiate\\source\\python\\python-core-language\\md\\"
# To process only ONE CODE file, Pass a value
# l_code_file = ''
l_code_file = "019_exceptions.py"
"""

# Test Set 2
code_file_folder = "C:\\Personal\\tinitiate\\source\\python\\python-oop\\code\\"
md_file_folder = "C:\\Personal\\tinitiate\\source\\python\\python-oop\\md\\"
# To process only ONE CODE file, Pass a value
# l_code_file = ''
l_code_file = "025_oop_vs_functional.py"
"""

code2md_gen(code_file_folder, md_file_folder, l_language, l_retain_yaml, l_code_file)







