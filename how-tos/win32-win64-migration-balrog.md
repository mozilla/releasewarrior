These steps are meant to be specifically for Firefox and Devedition 56.0b9.

# High-level steps

1. Create a new release in balrog for the migration 
2. Create a new balrog rule on the cdntest channels to point to to the release blob 

# Detailed descriptions

After we have b9 release blobs available in balrog we need to create a new release in balrog for win64 migration.  We also need to create a new watershed to map to this newly release in balrog
so win32 users with certain criteria will be updated to win64 firefox. See [bug 1393447](https://bugzilla.mozilla.org/show_bug.cgi?id=1393447) for more details.

Download [the script here](https://bug1393447.bmoattachments.org/attachment.cgi?id=8902074) to munge the release blobs called munge.py

Login to [balrog admin](https://aus4-admin.mozilla.org)

## Firefox beta

### Creating a new release  in balrog
```
Go to the [Firefox release for 56.0b9](https://aus4-admin.mozilla.org/releases#Firefox-56.0b9)
Select download to download the release blob
python munge.py /Users/kmoir/Downloads/Firefox-56.0b9-build1.json
which creates 
Firefox-56.0b9-build1-win64-migration.json
In balrog add a new release
Name is Firefox-56.0b9-build1-win64-migration
Product is firefox
upload your Firefox-56.0b9-build1-win64-migration.json file
```

### adding new rule
```
Add a rule to Firefox,beta-cdntest that points to that new rule
It should look like the top rule [in this screenshot](https://bug1393447.bmoattachments.org/attachment.cgi?id=8902907)
except it should be on the beta-cdntest rule
the mapping should be to b9 win64 migration release you just added
and the buildid should be updated to reflect the b9 buildid in the release blob
the comment should say b9 instead of b7
You don't require signoff for rules in test channels so it will just be added
```

## Devedition beta

### Modifying release blob
```
Go to the [Devedition release for 56.0b9](https://aus4-admin.mozilla.org/releases#Devedition-56.0b9)
Select download to download the release blob
python munge.py /Users/kmoir/Downloads/Devedition-56.0b9-build1.json
which creates 
Devedition-56.0b9-build1-win64-migration.json
In balrog add a new release
Name is Devedition-56.0b9-build1-win64-migration
Product is Firefox
upload your Devedition-56.0b9-build1-win64-migration.json file
```

### adding new rule 
```
Add a rule to Firefox,aurora-cdntest that points to that new rule
It should look like the [second rule in this screenshot](https://bug1393447.bmoattachments.org/attachment.cgi?id=8902907)
except it should be on the aurora-cdntest rule
the mapping should be to b9 win64 migration release you just added
and the buildid should be updated to reflect the b9 buildid in the release blob
the comment should say b9 instead of b7
You don't need signoff for rules on the test channel so it will just be added
```


