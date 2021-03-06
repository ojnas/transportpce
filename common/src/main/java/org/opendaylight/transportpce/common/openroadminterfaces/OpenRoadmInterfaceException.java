/*
 * Copyright © 2017 AT&T and others.  All rights reserved.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License v1.0 which accompanies this distribution,
 * and is available at http://www.eclipse.org/legal/epl-v10.html
 */

package org.opendaylight.transportpce.common.openroadminterfaces;

public class OpenRoadmInterfaceException extends Exception {

    public OpenRoadmInterfaceException(String message) {
        super(message);
    }

    public OpenRoadmInterfaceException(String message, Throwable cause) {
        super(message, cause);
    }
}
