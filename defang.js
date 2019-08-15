const defangIPaddr = address => {
    // return address.split('.').join('[.]');
    return address.replace(/[.]/g, '[.]');
};
