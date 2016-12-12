{
    # Date
    if ( $0 ~ /^date(.*)$/ ) {
        # Get date
        match($0, /^date: ([0-9]{4}\-[0-9]{2}\-[0-9]{2}).*$/, ary)
        print "Date: " ary[1]; 

    # Title 
    } else if ( $0 ~ /^title(.*)$/) {
        match($0, /^title: (.*)$/, ary)

        # Remove single/double quotes
        gsub(/'/, "", ary[1]);
        gsub(/"/, "", ary[1]);
        print "Title: " ary[1];

    # Author
    } else if ( $0 ~ /^author(.*)$/) {
        match($0, /^author: (.*)$/, ary)
        print "Author: " ary[1];

    # Handle available categories as tags
    } else if ($0 ~ /^categories:.*$/) {
        printf "Tags: "
        
        # Array index
        i = 0;

        # Read next line until new meta tag is found
        while ((getline line ) > 0) {
            # Read until new meta tag is found
            if ((line !~ /^.*\-.*$/) || (line ~ /^\-\-\-$/)) {
                output_string = ""
                # Print categories and the next exit loop
                for (j=0; j<i; j++)
                    
                    # Is this the last category
                    if (j+1 < i) 
                        output_string = output_string tolower(categories[j]) ", "

                    # Last category
                    else
                        output_string = output_string tolower(categories[j])
       
                # Remove last "," and add default category
                printf "%s\n", output_string
                printf "Category: blog\n\n"
                break
            }

            # Extract category
            match(line, /^.*\- (.*)$/, ary)
            categories[i] = ary[1]

            # Increase index
            i++;
        }

    }
}